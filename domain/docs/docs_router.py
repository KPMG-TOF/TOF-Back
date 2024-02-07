from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from domain.docs import docs_crud
from models import Info, Summary

router=APIRouter(
    prefix="/api/v1/docs"
)

@router.get("/{rfp_id}", status_code=status.HTTP_201_CREATED)
def rfp_analysis(rfp_id: int, db: Session=Depends(get_db)):
    docs_list = docs_crud.get_docs_list(db, rfp_id=rfp_id)

    return {
        "result":"success",
    }, docs_list