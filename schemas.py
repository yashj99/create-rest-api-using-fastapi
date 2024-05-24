from pydantic import BaseModel

class Class(BaseModel):
    class_name:str
    section:str
    year:int
    count:int