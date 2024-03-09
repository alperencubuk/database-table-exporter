from pydantic import BaseModel

from source.app.export.enums import FileType


class ExportRequest(BaseModel):
    database: str
    table: str
    fields: list[str] | None = None
    file_type: FileType = FileType.CSV


class ExportResponse(BaseModel):
    task_id: str
