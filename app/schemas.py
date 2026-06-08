from pydantic import BaseModel, ConfigDict

class ProjectCreate(BaseModel):
    name: str
    status: str = "Planned"

class ProjectResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    status: str
