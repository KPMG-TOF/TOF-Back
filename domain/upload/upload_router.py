from fastapi import APIRouter, Depends, HTTPException, Form, File, UploadFile 
from sqlalchemy.orm import Session
from sqlalchemy import String
from starlette import status
from typing import List
from datetime import datetime
from database import get_db
from domain.upload import upload_schema, upload_crud

router = APIRouter(
    prefix="/api/v1/upload"
)

@router.post("/rfp", status_code=201)
def upload_create(files: List[UploadFile]  = File(...), db: Session=Depends(get_db)):
    for file in files:
        rfp_id = upload_crud.upload_rfp(db, file=file.filename)

    return{
        "result":"success",
        "rfp_id": rfp_id
    }

@router.post("/doc", status_code=201)
def upload_create(files: List[UploadFile] = File(...), rfp_id: int = Form(...), date: datetime = Form(...), writer: str =Form(...), db: Session = Depends(get_db)):
    for file in files:
        upload_crud.upload_doc(db, file=file.filename, rfp_id=rfp_id, date=date, writer=writer)
        
    return{
        "result":"success"
    }