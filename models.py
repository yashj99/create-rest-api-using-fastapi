
from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from database import Base

class Class(Base):
    __tablename__ = 'class'
    id = Column(Integer, primary_key=True, nullable=False)
    class_name = Column(String, nullable=False)
    section = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    count = Column(Integer,nullable=False)
