# Portfolio FastAPI backend

Quick scaffold for a portfolio backend using FastAPI + SQLModel (SQLite).

Setup (Windows):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Files:

- [app/main.py](app/main.py) - app entry
- [app/db.py](app/db.py) - database engine + init
- [app/models.py](app/models.py) - SQLModel models
- [app/routers](app/routers) - routers for projects/contact/health/profile/skills

Frontend:

- frontend/index.html - minimal single-file frontend that calls the API (open directly or serve with a simple static server)

To test frontend quickly (from workspace root):

```powershell
# serve frontend on port 8001 with Python
python -m http.server 8001 -d frontend
# then open http://localhost:8001
```
