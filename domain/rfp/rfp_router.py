from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from database import get_db
from domain.rfp import rfp_crud
from models import Info, Summary


router=APIRouter(
    prefix="/api/v1/rfp"
)

@router.get("/list")
def get_rfp_list(db: Session = Depends(get_db)):
    list = rfp_crud.get_rfp_list(db)
    if list:
        return {"result":"success"}, list
    else:
        return {"result":"error"}


@router.post("/update/progress/{rfp_id}", status_code = 200)
def rfp_update(rfp_id: int, db: Session = Depends(get_db)):
    response = rfp_crud.update_rfp_progress(db, rfp_id)
    if response:
        return {"result":"success"}
    else:
        return {"result":"error"}

@router.post("/delete/{rfp_id}", status_code=200)
def delete_rfp(rfp_id: int, db: Session = Depends(get_db)):
    success = rfp_crud.delete_rfp(db, rfp_id)
    if success:
        return {"result": "success", "message": f"RFP with ID {rfp_id} deleted successfully"}
    else:
        return {"result": "error", "message": f"RFP with ID {rfp_id} not found"}
