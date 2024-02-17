from datetime import datetime
from sqlalchemy.orm import Session
from domain.upload.upload_schema import UploadRFP
from domain.rfp import rfp_summary

from models import RFP, Info, Summary, Subject, Requirement, Doc

def upload_rfp(db: Session, file: str):
    db_upload = RFP(file=file, upload_date="2024-02-15")
    db.add(db_upload)
    db.commit()

    # rfp info, summary
    json = rfp_summary.fine_tuning_summary(file)


    info = json["info"]
    summary = json["summary"]


    db_info = Info(title=info["title"], company=info["company"],  cost=info["cost"], rfp_id=db_upload.id)
    db.add(db_info)
    db.commit()

    # summary db
    db_summary = Summary(
                         start_date=summary["start_date"], 
                         end_date=summary["end_date"], 
                         rfp_id=db_upload.id)
    db.add(db_summary)
    db.commit()

    # subject, requirement 추출 필요
    # subject db
    list_subject = summary["subject"]
    for subject in list_subject:
        db_subject = Subject(content=subject, summary=db_summary)
        print(subject, db_subject)
        db.add(db_subject)
        db.commit()

    # requirement db
    list_requirement = summary["requirement"]
    for requirement in list_requirement:
        db_requirement = Requirement(content=requirement, summary=db_summary)
        db.add(db_requirement)
        db.commit()

    return db_upload.id

def upload_doc(db: Session, file: str, date: datetime, writer: str, rfp_id: int):
    db_upload = Doc(file=file, date=date, rfp_id=rfp_id, writer=writer)
    db.add(db_upload)
    db.commit()

def download_file(db: Session, id: int):
    file_info = db.query(RFP).filter(RFP.id == id).first()
    file_name = file_info.file

    return file_name