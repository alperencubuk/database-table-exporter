from os import getcwd, path

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse

from source.app.download.schemas import FileDownload
from source.core.exceptions import not_found

download_router = APIRouter(prefix="/download", tags=["download"])


@download_router.get("/{file_name}", response_class=FileResponse)
async def file_download(request: FileDownload = Depends()):
    file_path = f"{getcwd()}/files/{request.file_name}"
    if path.exists(file_path):
        return file_path
    return not_found(f"File '{request.file_name}' not found")
