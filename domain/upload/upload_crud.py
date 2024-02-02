from datetime import datetime
from sqlalchemy.orm import Session
from domain.upload.upload_schema import UploadRFP
from models import RFP, Info, Summary

def upload_rfp(db: Session, file: str):
    db_upload = RFP(file=file, upload_date=datetime.now())
    db.add(db_upload)
    db.commit()

    # info, summary 추출 필요
    # info db
    db_info = Info(title=file, company="sso", industry="dev", cost=12342, rfp_id=db_upload.id)
    db.add(db_info)
    db.commit()

    # summary db
    db_summary = Summary(size=5453, start_date=datetime.now(), end_date=datetime.now(), rfp_id=db_upload.id)
    db.add(db_summary)
    db.commit()

    print(file)