from datetime import datetime
from sqlalchemy.orm import Session
from domain.upload.upload_schema import UploadRFP
from models import RFP, Info, Summary, Subject, Requirement, Doc

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

    # subject, requirement 추출 필요
    # subject db
    list_subject = ["클라우드가 필요함", "클라우드가 궁금함", "어쩌구"]
    for subject in list_subject:
        db_subject = Subject(content=subject, summary=db_summary)
        print(subject, db_subject)
        db.add(db_subject)
        db.commit()

    # requirement db
    list_requirement = ["보안이 필요함", "보안이 궁금함", "어쩌구"]
    for requirement in list_requirement:
        db_requirement = Requirement(content=requirement, summary=db_summary)
        db.add(db_requirement)
        db.commit()

def upload_doc(db: Session, file: str, rfp_id: int):
    db_upload = Doc(file=file, date=datetime.now(), rfp_id=rfp_id, writer="작성자")
    db.add(db_upload)
    db.commit()