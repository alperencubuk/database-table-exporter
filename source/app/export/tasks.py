import csv
from os import getcwd, path

import openpyxl
import psycopg
from psycopg import sql

from source.app.export.enums import FileType
from source.core.celery import celery_app
from source.core.settings import settings


@celery_app.task
def export_task(
    database: str, table: str, fields: list[str] | None, file_format: FileType
) -> None:
    query = sql.SQL("select {fields} from {table}").format(
        fields=(
            sql.SQL(", ").join(sql.Identifier(field) for field in fields)
            if fields
            else sql.SQL("*")
        ),
        table=sql.Identifier(table),
    )

    with psycopg.connect(settings.DATABASE_URIS[database]) as conn:
        with conn.cursor() as cur:
            cur.execute(query.as_string(conn))
            fields = [desc[0] for desc in cur.description]
            rows = cur.fetchall()

    file_name = path.join(getcwd(), "files", f"{export_task.request.id}")

    if file_format == FileType.CSV:
        with open(f"{file_name}.csv", "w+") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(fields)
            csv_writer.writerows(rows)

    elif file_format == FileType.EXCEL:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.append(fields)
        ws.append(rows)
        wb.save(f"{file_name}.xlsx")
