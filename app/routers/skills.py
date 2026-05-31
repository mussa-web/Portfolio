from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from sqlmodel import select
from app.db import get_session
from app.models import Skill

router = APIRouter()


@router.get("/", response_model=List[Skill])
def list_skills(category: Optional[str] = Query(None), session=Depends(get_session)):
    statement = select(Skill)
    if category:
        statement = statement.where(Skill.category == category)
    results = session.exec(statement).all()
    return results


@router.get("/{skill_id}", response_model=Skill)
def get_skill(skill_id: int, session=Depends(get_session)):
    skill = session.get(Skill, skill_id)
    if not skill:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill
