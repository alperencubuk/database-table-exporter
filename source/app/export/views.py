from fastapi import APIRouter

from source.app.export.schemas import ExportRequest, ExportResponse
from source.app.export.tasks import export_task
from source.core.exceptions import not_found
from source.core.settings import settings

export_router = APIRouter(prefix="/export", tags=["export"])


@export_router.post("/", response_model=ExportResponse)
async def export(request: ExportRequest) -> dict:
    if not settings.DATABASE_URIS.get(request.database):
        return not_found(f"Database '{request.database}' not found")
    task = export_task.delay(
        database=request.database,
        table=request.table,
        fields=request.fields,
        file_format=request.file_type,
    )
    return {"task_id": task.id}
