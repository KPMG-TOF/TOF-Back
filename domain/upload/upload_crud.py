from datetime import datetime
from sqlalchemy.orm import Session
from domain.upload.upload_schema import UploadRFP
from domain.rfp import rfp_summary
from models import RFP, Info, Summary, Subject, Requirement, Doc

def upload_rfp(db: Session, file: str):
    db_upload = RFP(file=file, upload_date=datetime.now())
    db.add(db_upload)
    db.commit()

    # json = rfp_summary.fine_tuning_summary("./RFP/RFP1.hwp")

    json = {'info': {'company': 'KEB 하나은행', 'cost': '제안사 제안 가격', 'title': 'KEB 하나은행 GLN(Global Loyalty Nework) 플랫폼 구축을 위한 클라우드 서비스 제안요청서'}, 'summary': {'start_date': '2018.12', 'end_date': '2019.03', 'subject': ['안정적인 클라우드 인프라 구축', '클라우드 기반 전자결제 서비스 구성', '고가용성 및  편의성을 고려한 개발 및 운영 환경 제공'], 'requirement': ['국제사회적', '환경적 책임', '프로젝트 관리 및 품질보증', '시스템 개발 및 테스트', '시험운영지원', '교육', '레퍼런스 데이터(이미지', '문서 등) 변환', '데이 터 입력', '데이터 출력', '인터페이스', '보안', '비즈니스 로직', '운영 관리', '서비스 준비 및 종료', '시간  및 리소스 관리', '관련 법규 준수', '리스크 관리']}}

    print(json)
    info = json["info"]
    summary = json["summary"]

    # info, summary 추출 필요
    # info db
    cost_value = info["cost"]
    if cost_value.isdigit():
        cost = int(cost_value)
    else:
        cost = -1

    db_info = Info(title=info["title"], company=info["company"],  cost=cost, rfp_id=db_upload.id)
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