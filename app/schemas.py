from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        from_attributes = True


class ContestCreate(BaseModel):
    title: str
    description: str
    start_time: datetime
    end_time: datetime


class ContestResponse(BaseModel):
    id: int
    title: str
    description: str
    start_time: datetime
    end_time: datetime
    created_by: int

    class Config:
        from_attributes = True

class ProblemCreate(BaseModel):
    contest_id: int
    title: str
    description: str
    difficulty: str


class ProblemResponse(BaseModel):
    id: int
    contest_id: int
    title: str
    description: str
    difficulty: str

    class Config:
        from_attributes = True

class TestCaseCreate(BaseModel):
    problem_id: int
    input_data: str
    expected_output: str
    is_visible: int


class TestCaseResponse(BaseModel):
    id: int
    problem_id: int
    input_data: str
    expected_output: str
    is_visible: int

    class Config:
        from_attributes = True