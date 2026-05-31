from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Project(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    url: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    message: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


class Skill(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    category: Optional[str] = None  # e.g. 'data-science', 'network-marketing'
    level: Optional[str] = None


class Profile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    full_name: str
    headline: Optional[str] = None
    bio: Optional[str] = None
    picture_path: Optional[str] = None  # served from /static/
    website: Optional[str] = None
    linkedin: Optional[str] = None
    twitter: Optional[str] = None
