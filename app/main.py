
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from prometheus_fastapi_instrumentator import Instrumentator

from app import models, schemas
from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Construction API")
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"status": "running", "version": "1.0.0"}


@app.get("/projects", response_model=list[schemas.ProjectResponse])
def list_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()


@app.post("/projects", response_model=schemas.ProjectResponse, status_code=201)
def create_project(
    project: schemas.ProjectCreate,
    db: Session = Depends(get_db),
):
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
