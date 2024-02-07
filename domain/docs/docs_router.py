from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from domain.analysis import analysis_schema, analysis_crud
from models import Info, Summary

router=APIRouter(
    prefix="/api/v1/reference"
)

@router.get("/{rfp_id}")
def question_list(db: Session = Depends(get_db)):
    _question_list = analysis_crud.get_info_list(db)
    return _question_list