from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/problems/create", response_model=schemas.ProblemResponse)
def create_problem(problem: schemas.ProblemCreate, db: Session = Depends(get_db)):
    new_problem = models.Problem(**problem.dict())
    db.add(new_problem)
    db.commit()
    db.refresh(new_problem)
    return new_problem


@router.get("/problems", response_model=list[schemas.ProblemResponse])
def get_problems(db: Session = Depends(get_db)):
    return db.query(models.Problem).all()


@router.get("/contest/{contest_id}/problems", response_model=list[schemas.ProblemResponse])
def get_contest_problems(contest_id: int, db: Session = Depends(get_db)):
    return db.query(models.Problem).filter(models.Problem.contest_id == contest_id).all()