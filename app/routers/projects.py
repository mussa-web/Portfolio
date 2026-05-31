from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlmodel import select
from app.db import get_session
from app.models import Project

router = APIRouter()


@router.get("/", response_model=List[Project])
def list_projects(session=Depends(get_session)):
    statement = select(Project).order_by(Project.created_at.desc())
    results = session.exec(statement).all()
    return results


@router.get("/{project_id}", response_model=Project)
def get_project(project_id: int, session=Depends(get_session)):
    project = session.get(Project, project_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project


@router.post("/", response_model=Project)
def create_project(project: Project, session=Depends(get_session)):
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
