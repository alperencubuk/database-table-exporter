from celery.result import AsyncResult
from fastapi import APIRouter, Depends

from source.app.status.schemas import StatusRequest, StatusResponse

status_router = APIRouter(prefix="/status", tags=["status"])


@status_router.get("/{task_id}", response_model=StatusResponse)
async def status(
    request: StatusRequest = Depends(),
) -> dict:
    return {"status": AsyncResult(request.task_id).state}
