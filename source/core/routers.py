from fastapi import APIRouter

from source.app.download.views import download_router
from source.app.export.views import export_router
from source.app.status.views import status_router

api_router = APIRouter()

api_router.include_router(download_router)
api_router.include_router(export_router)
api_router.include_router(status_router)
