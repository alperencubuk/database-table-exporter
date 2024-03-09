from pydantic import BaseModel


class StatusRequest(BaseModel):
    task_id: str


class StatusResponse(BaseModel):
    status: str
