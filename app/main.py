from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.db import init_db
from app.routers import projects, contact, health, profile, skills
from app.sample_data import create_sample_projects, create_sample_profile_and_skills

app = FastAPI(title="Portfolio API")


@app.on_event("startup")
def on_startup():
    init_db()
    # create sample data if missing
    create_sample_projects()
    create_sample_profile_and_skills()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# serve a simple static folder for images / frontend assets
app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(projects.router, prefix="/projects", tags=["projects"])
app.include_router(contact.router, prefix="/contact", tags=["contact"])
app.include_router(health.router, prefix="", tags=["health"])
app.include_router(profile.router, prefix="/profile", tags=["profile"])
app.include_router(skills.router, prefix="/skills", tags=["skills"])


@app.get("/")
def root():
    return {"message": "Portfolio API running"}
