from pydantic import BaseModel


class HealthSchema(BaseModel):
    health: bool
