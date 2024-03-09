from pydantic import BaseModel


class FileDownload(BaseModel):
    file_name: str
