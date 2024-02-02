from models import Info, Summary
from domain.analysis.analysis_schema import Reference, Priority, Competivity, Workforce, Task
from sqlalchemy.orm import Session
import random
from datetime import datetime

def get_info_list(db:Session):
    info_list = db.query(Info)\
        .order_by(Info.id.desc())\
        .all()
    
    return info_list

def get_info(db: Session, rfp_id: int):
    info = db.query(Info).get(rfp_id)
    return info

def get_summary(db: Session, rfp_id: int):
    summary = db.query(Summary).get(rfp_id)
    subjects = [subject.content for subject in summary.subjects]
    requirements = [requirement.content for requirement in summary.requirements]

    summary.subject = subjects
    summary.requirement = requirements

    return summary

def get_reference(rfp_id: int):
    list_reference = []

    for _ in range(random.randrange(1,5)):
        list_reference.append(Reference(rfp_id=random.randrange(1,10), title="fake ref", end_date=datetime.now(), manager="sso", similarity=random.randrange(1,100)))
        
    return list_reference

def get_priority(rfp_id: int):
    list_priority=[]
    for _ in range(random.randrange(1,5)):
        order = random.randrange(1,20)
        title = "priority"

        list_priority.append(Priority(order= order, title= title))

    return list_priority

def get_competivity(rfp_id: int):
    list_competivity=[]
    for _ in range(random.randrange(1,5)):
        order = random.randrange(1,1000)
        title = "competivity"   

        list_competivity.append(Competivity(order= order, title= title))

    return list_competivity

def get_workforce(rfp_id: int):
    list_workforce = []
    
    for _ in range(random.randrange(1,5)):
        count = random.randrange(1,1000)
        category = "workforce"

        list_workforce.append(Workforce(count=count, category=category))

    return list_workforce

def get_tasks(rfp_id: int):
    priority = get_priority(rfp_id)
    competivity = get_competivity(rfp_id)
    workforce = get_workforce(rfp_id)

    return Task(priority=priority, competivity=competivity, workforce=workforce)
