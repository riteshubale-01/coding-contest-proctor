from fastapi import FastAPI

app = FastAPI(
    title="Coding Contest Proctor API",
    description="Backend API for coding contest platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Coding Contest Proctor API is running"}
