from fastapi import APIRouter, Depends
from sqlmodel import select
from app.db import get_session
from app.models import Profile

router = APIRouter()


@router.get("/", response_model=Profile)
def get_profile(session=Depends(get_session)):
    profile = session.exec(select(Profile)).first()
    if not profile:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
