from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    status: str = "Planned"

class ProjectResponse(BaseModel):
    id: int
    name: str
    status: str

    class Config:
        from_attributes = True