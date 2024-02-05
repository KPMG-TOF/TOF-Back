from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from domain.analysis import analysis_schema, analysis_crud
from models import Info, Summary

router=APIRouter(
    prefix="/api/v1/main"
)

# Test
@router.get("/list", response_model=list[analysis_schema.Info])
def question_list(db: Session = Depends(get_db)):
    _question_list = analysis_crud.get_info_list(db)
    return _question_list

# Test
@router.get("/detail/{rfp_id}", response_model=analysis_schema.Info)
def rfp_detail(rfp_id: int, db: Session = Depends(get_db)):
    rfp_info = analysis_crud.get_info(db, rfp_id=rfp_id)
    return rfp_info

@router.get("/analysis/{rfp_id}", status_code=status.HTTP_201_CREATED)
def rfp_analysis(rfp_id: int, db: Session=Depends(get_db)):
    rfp_info = analysis_crud.get_info(db, rfp_id=rfp_id)
    rfp_summary = analysis_crud.get_summary(db, rfp_id=rfp_id)
    rfp_reference = analysis_crud.get_reference(rfp_id=rfp_id)
    rfp_tasks = analysis_crud.get_tasks(rfp_id=rfp_id)

    return {
        "result":"success",
        "info": rfp_info,
        "summary": rfp_summary,
        "reference": rfp_reference,
        "tasks": rfp_tasks
    }