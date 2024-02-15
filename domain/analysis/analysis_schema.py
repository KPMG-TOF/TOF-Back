from pydantic import BaseModel
from typing import Union, List

class Info(BaseModel):
    company: str
    cost: int
    title: str

# class Summary(BaseModel):
#     start_date: str
#     end_date: str
#     subject: List[str]
#     requirement: List[str]

class Summary(BaseModel):
    start_date: str
    end_date: str
    subject: Union[List[str], None] = None
    requirement: Union[List[str], None] = None

class Reference(BaseModel):
    rfp_id: int
    title: str
    end_date: str
    manager: str
    keyword: List[str]
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
    priority: List[Priority]
    competivity: List[Competivity]
    workforce: List[Workforce]

class Analysis(BaseModel):
    info: Info
    summary: Summary
    reference: Union[List[Reference], None] = None
    tasks: Union[Task, None] = None

