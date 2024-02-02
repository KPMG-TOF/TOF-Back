from pydantic import BaseModel
from datetime import datetime
from typing import Union, List

class Info(BaseModel):
    company: str
    industry: str
    cost: int
    title: str

# class Summary(BaseModel):
#     size: int
#     start_date: datetime
#     end_date: datetime
#     subject: List[str]
#     requirement: List[str]

class Summary(BaseModel):
    size: int
    start_date: datetime
    end_date: datetime
    subject: Union[List[str], None] = None
    requirement: Union[List[str], None] = None

class Reference(BaseModel):
    rfpId: int
    title: str
    end_date: datetime
    manager: str
    similarity: float

class Priority(BaseModel):
    order: int
    title: str

class Competivity(BaseModel):
    order: int
    title: str

class Workforce(BaseModel):
    count: int
    category: str

class Task(BaseModel):
    priority: Priority
    competivity: Competivity
    workforce: Workforce

class Analysis(BaseModel):
    info: Info
    summary: Summary
    reference: Union[Reference, None] = None
    tasks: Union[Task, None] = None

