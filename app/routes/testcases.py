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


@router.post("/testcases/create", response_model=schemas.TestCaseResponse)
def create_testcase(testcase: schemas.TestCaseCreate, db: Session = Depends(get_db)):

    new_testcase = models.TestCase(**testcase.dict())

    db.add(new_testcase)
    db.commit()
    db.refresh(new_testcase)

    return new_testcase


@router.get(
    "/problem/{problem_id}/visible-testcases",
    response_model=list[schemas.TestCaseResponse]
)
def get_visible_testcases(problem_id: int, db: Session = Depends(get_db)):
    return db.query(models.TestCase).filter(
        models.TestCase.problem_id == problem_id,
        models.TestCase.is_visible == 1
    ).all()


@router.get(
    "/problem/{problem_id}/testcases",
    response_model=list[schemas.TestCaseResponse]
)
def get_all_testcases(problem_id: int, db: Session = Depends(get_db)):
    return db.query(models.TestCase).filter(
        models.TestCase.problem_id == problem_id
    ).all()