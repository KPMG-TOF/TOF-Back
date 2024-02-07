from models import RFP, Doc
from domain.analysis.analysis_schema import Reference, Priority, Competivity, Workforce, Task
from sqlalchemy.orm import Session
import random
from datetime import datetime
from fastapi import HTTPException, status


def get_docs_list(db: Session, rfp_id: int):
    rfp = db.query(RFP).get(rfp_id)
    docs = [doc.file for doc in rfp.docs]

    return docs