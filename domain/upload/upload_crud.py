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
                    "국내외 네트워크망 확장 연계 고려",
                    "물리적/논리적 시스템 구성에 있어 관련 국내 감독규정 준수",
                    "인프라 리소스 및 로그 모니터링 진단 툴 제공",
                    "교육/운영지원/기술이전 등 기업 활동 지원",
                    "프로젝트 관리 및 품질보증 방안 제시",
                    "리스크 관리방안 제시"
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

#     json = {
#     "info": {
#       "company": "방위사업청",
#       "cost": "3,004,000,000원 (총액 계약, 부가가치세 포함)",
#       "title": "24년 사이버보안 취약점 진단사업"
#     },
#     "summary": {
#       "start_date": "계약일",
#       "end_date": "계약일로부터 2024년 12월 20일까지",
#       "subject": [
#         "’22년 ~ ’24년 진단결과 이행점검 및 이행 지원",
#         "보유 정보자산 기술적 취약점 진단",
#         "주요 운용서버 및 PC 등 정밀진단 수행",
#         "인터넷 정보시스템에 대한 모의해킹(외부, 내부)",
#         "해킹메일 대응훈련",
#         "사용자 PC 교육자료 및 점검용 파일 제작",
#         "방산(협력)업체 정보시스템 보안 강화를 위한 개선안 도출",
#         "대상업체에 대한 사이버보안 발전방향 제시"
#       ],
#       "requirement": [
#         "시업 수행을 위해 필요한 컨설팅 수행범위, 내용, 절차 등 요건에 대한 요구사항을 기술함",
#         "정보 자산의 기밀성과 무결성을 확보하기 위해 사업 수행 시 인적, 물적 보안 및 취득한 정보에 대한 보안 요구사항을 기술함",
#         "목표 사업의 원활한 수행 및 운영을 위해 관리가 필요한 품질 항목, 품질평가 대상 및 목표에 대한 요구사항을 기술함",
#         "사업의 원활한 수행을 위한 관리 방법 및 추진 단계별 수행방안에 대한 요구사항을 기술함",
#         "사업 추진 시 필요한 지원사항 및 방안에 대한 요구사항을 기술함"
#       ]
#     }
#   }
    
  #   json = {
  #   "info": {
  #     "company": "한국통신사업자연합회",
  #     "cost": "공개경쟁입찰",
  #     "title": "KTOA 인터넷 트래픽 정산 시스템 H/W구축"
  #   },
  #   "summary": {
  #     "start_date": "계약일",
  #     "end_date": "계약일로부터 6개월",
  #     "subject": [
  #       "ISP 사업자의 네트워크 시스템과 연동할 수 있도록 체계적이고 일관성 있게 추진",
  #       "향후, 시스템의 확장과 정보관리 등 정보화 여건, 효과성, 효율성, 기반환경, 현황 등을 고려하여 구축",
  #       "향후 트래픽 증대에 따른 확장성을 고려하여 개발 및 구축과 테스트가 진행되어야 함",
  #       "ISP 사업자에게 정산해야 할 트래픽을 통보하고 통계 데이터를 작성해야 한다."
  #     ],
  #     "requirement": [
  #       "납품 및 설치는 계약일로부터 3주 이내에 이루어져야 하며, 본 사업 수행시 도입괴는 모든 장비는 8년 이상 보장되어야 한다.",
  #       "시스템 요구사항, H/W, S/W등 본 사업 수행에 필요한 일체에 대하여 사양,수량 및 선정근거를 제시하여야 한다",
  #       "전산실 교수사항, 전산실은 365일 24시간 시스템 운영 및 보안을 고려하여 설치되어야 한다.",
  #       "지원 요구사항, 연동대상 사업자에 대한 네트워크 연결 및 본 사업과 관련 부대설치 공사 일체를 제공해야 한다."
  #     ]
  #   }
  # }
    
#     json = {
#     "info": {
#       "company": "한국과학기술정보연구원",
#       "cost": "금 360,000,000원(부가세포함)",
#       "title": "연구용 서버 취약점 보안진단 솔루션 구매"
#     },
#     "summary": {
#       "start_date": "계약 체결일",
#       "end_date": "계약 체결일로부터 3개월이내",
#       "subject": [
#         "연구용 서버 보안수준 자가진단 서비스 수행을 위해 구현된 자가진단 신청",
#         "구축 시스템에서 도입 솔루션을 제어",
#         "솔루션이 제공하는 진단항목을 서비스 요구사항에 따라 분류, 관리 및 최적화",
#         "연구용 서버 자가진단 이력 및 분석 결과/조치방안에 대한 별도 DB 구축 지원"
#       ],
#       "requirement": [
#         "모든 솔루션은 납품 완료시 7일 이내 제조사의 제품 공급 확양서 등 원본 1부를 제출해야 한다.",
#         "도입 솔루션은 旣 구축 시스템(연구용 서버 보안수준 자가진단 시스템)과 상호간에 완벽한 호환성・연계성을 반드시 확보해야 한다.",
#         "연구용 서버 취약점 보안 진단 솔루션의 기본 기능과 필요 사항들을 계약자는 함께 제공해야 한다.",
#         "설치 장소는 서버실, 설치기간은 설치 및 안정화 기간을 고려해 3개월 이내로 한다.",
#         "납품 검수완료 후 지정 소프트웨어의 유지보수 기간 1년동안은 무상으로 해야한다.",
#         "도입 솔루션의 모든 부품은 일체 정품으로 납부하며, 명시되지 않은 사항은 관리 감독관과 협의한다."
#       ]
#     }
#   }

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