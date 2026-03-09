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


@router.post("/contest/create", response_model=schemas.ContestResponse)
def create_contest(contest: schemas.ContestCreate, db: Session = Depends(get_db)):

    new_contest = models.Contest(
        title=contest.title,
        description=contest.description,
        start_time=contest.start_time,
        end_time=contest.end_time,
        created_by=1
    )

    db.add(new_contest)
    db.commit()
    db.refresh(new_contest)

    return new_contest