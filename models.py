from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class RFP(Base):
    __tablename__="rfp"

    id=Column(Integer, primary_key=True)
    file=Column(String, nullable=False)
    progress = Column(Boolean, default=False, nullable=False)
    upload_date = Column(DateTime, nullable=False)

class Doc(Base):
    __tablename__="doc"

    id=Column(Integer, primary_key=True)
    file=Column(String, nullable=False)
    date = Column(DateTime)
    writer = Column(String)
    rfp=relationship("RFP", backref="docs")

    rfp_id = Column(Integer, ForeignKey("rfp.id"))

class Info(Base):
    __tablename__ = "info"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    company = Column(String, nullable=False)
    industry = Column(String, nullable=False)
    cost = Column(Integer, nullable=False)

    rfp_id = Column(Integer, ForeignKey("rfp.id"))

class Summary(Base):
    __tablename__="summary"

    id = Column(Integer, primary_key=True)  
    size = Column(String, nullable=False)
    start_date = Column(String, nullable=False)
    end_date = Column(String, nullable=False)
    
    rfp_id = Column(Integer, ForeignKey("rfp.id"))

class Subject(Base):
    __tablename__="subject"
    
    id = Column(Integer, primary_key=True)  
    summary=relationship("Summary", backref="subjects")
    content = Column(String, nullable=False)

    summary_id = Column(Integer, ForeignKey("summary.id"))

class Requirement(Base):
    __tablename__="requirement"

    id = Column(Integer, primary_key=True)  
    summary=relationship("Summary", backref="requirements")
    content = Column(String, nullable=False)

    summary_id = Column(Integer, ForeignKey("summary.id"))


