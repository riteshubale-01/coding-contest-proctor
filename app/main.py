from fastapi import FastAPI
from .database import engine, Base

app = FastAPI(
    title="Coding Contest Proctor API",
    description="Backend API for coding contest platform",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Coding Contest Proctor API is running"}
