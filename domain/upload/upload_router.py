from fastapi import APIRouter, Depends, HTTPException, File, UploadFile 
from sqlalchemy.orm import Session
from starlette import status

from database import get_db
from domain.upload import upload_schema, upload_crud

router = APIRouter(
    prefix="/api/v1/upload"
)

@router.post("/rfp", status_code=201)
def upload_create(file: UploadFile = File(...), db: Session=Depends(get_db)):
    
    upload_crud.upload_rfp(db, file=file.filename)
    return{
        "result":"success"
    }
