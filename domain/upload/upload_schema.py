from pydantic import BaseModel, field_validator
from datetime import datetime

class UploadRFP(BaseModel):
    file: str
    time: datetime

    @field_validator('file')
    def not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값은 허용되지 않습니다.')
        return v