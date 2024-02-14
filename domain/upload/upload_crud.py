from datetime import datetime
from sqlalchemy.orm import Session
from domain.upload.upload_schema import UploadRFP
from domain.rfp import rfp_summary

from models import RFP, Info, Summary, Subject, Requirement, Doc

def upload_rfp(db: Session, file: str):
    db_upload = RFP(file=file, upload_date=datetime.now())
    db.add(db_upload)
    db.commit()

    # rfp info, summary
    # json = rfp_summary.fine_tuning_summary("D:/TOF-Back/domain/rfp/summary/RFP/RFP1.hwp")
    json = {
                "info": {
                    "company": "KEB 하나은행",
                    "cost": "제안사 제안 가격",
                    "title": "KEB 하나은행 GLN(Global Loyalty Nework) 플랫폼 구축을 위한 클라우드 서비스 제안요청서"
                },
                "summary": {
                    "start_date": "2018.12",
                    "end_date": "2019.3",
                    "subject": [
                    "안정적인 클라우드 인프라 구축",
                    "클라우드 기반 전자결제 서비스 구성",
                    "고가용성 및 편의성을 고려한 개발 및 운영 환경 제공"
                    ],
                    "requirement": [
                    "국내외 네트워크를 통한 전산시스템 연동 가능여부 및 연동 방안",
                    "원격 및 On-Site 작업가능 여부 및 방안",
                    "국내외 로그 및 모니터링 정보를 제공받을 수 있는 방안",
                    "인프라 및 개발운영 전반에 대한 프로젝트 관리 방안",
                    "최종 서비스 안정적 수행 및 관리할 수 있는 방안"
                    ]
                }
            }
    
    # json = {
    #         "info": {
    #             "company": "국립국어원 어문연구실 한국어진흥과",
    #             "cost": "450000000",
    #             "title": "2022년 개방형 한국어 통합 사전 시스템 클라우드 전환"
    #         },
    #         "summary": {
    #             "start_date": "계약 후",
    #             "end_date": "계약 후~160일",
    #             "subject": [
    #             "한국어기초사전 및 다국어사전 시스템 개선 및 클라우드 전환",
    #             "멀티미디어 자료 나눔터 개선 및 클라우드 전환",
    #             "대구 전산센터 이전을 위한 클라우드 전환"
    #             ],
    #             "requirement": [
    #             "한국어기초사전 및 다국어사전 시스템 개선 및 클라우드 전환",
    #             "멀티미디어 자료 나눔터 개선 및 클라우드 전환",
    #             "대구 전산센터 이전을 위한 클라우드 전환"
    #             ]
    #         }
    #     }


    info = json["info"]
    summary = json["summary"]

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

def download_file(db: Session, id: int):
    file_info = db.query(RFP).filter(RFP.id == id).first()
    file_name = file_info.file

    return file_name