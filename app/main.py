from fastapi import FastAPI
from .database import engine, Base
from . import models
from .routes import users, contests

app = FastAPI(
    title="Coding Contest Proctor API",
    description="Backend API for coding contest platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(users.router)
app.include_router(contests.router)

@app.get("/")
def root():
    return {"message": "Coding Contest Proctor API is running"}
