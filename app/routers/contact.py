from fastapi import APIRouter, Depends
from app.models import Contact
from app.db import get_session

router = APIRouter()


@router.post("/", response_model=Contact)
def submit_contact(payload: Contact, session=Depends(get_session)):
    session.add(payload)
    session.commit()
    session.refresh(payload)
    return payload
