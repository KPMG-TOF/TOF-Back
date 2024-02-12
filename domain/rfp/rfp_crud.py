from models import RFP, Doc
from sqlalchemy.orm import Session
import random
from datetime import datetime
from fastapi import HTTPException, status

def get_rfp_list(db:Session):
    rfp_list = db.query(RFP)\
        .order_by(RFP.id.desc())\
        .all()
    
    return rfp_list

def update_rfp_progress(db:Session, rfp_id:int):
    rfp = db.query(RFP).get(rfp_id)
    if rfp:
        rfp.progress = not rfp.progress
        db.commit()
        return True
    else:
        return False

def delete_rfp(db: Session, rfp_id: int):
    rfp = db.query(RFP).get(rfp_id)
    if rfp:
        db.delete(rfp)
        db.commit()
        return True
    else:
        return False
    
def get_progress_reference(db: Session):
    progress_list = db.query(RFP).filter(RFP.progress==True)
    for progress in progress_list:
        print(progress.file)

    