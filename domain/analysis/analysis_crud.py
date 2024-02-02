from models import Info
from sqlalchemy.orm import Session

def get_info_list(db:Session):
    info_list = db.query(Info)\
        .order_by(Info.id.desc())\
        .all()
    
    return info_list

def get_info(db: Session, rfp_id: int):
    info = db.query(Info).get(rfp_id)
    return info