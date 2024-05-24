from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from database import get_db,engine
from schemas import Class
import psycopg2
from psycopg2.extras import RealDictCursor
import time
import models

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='database_for_fast_api', user='postgres',
                                password='12345', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print('Database succesfully connected')
        break
    except Exception as error:
        print('connection failed')
        print('error:', error)
        time.sleep(3)

app = FastAPI()

models.Base.metadata.create_all(bind= engine)

@app.get("/")
def posts():
    return {"message": "this is working"}

@app.get("/classes")
def get(db: Session = Depends(get_db)):
    all_classes = db.query(models.Class).all()
    return all_classes

# Endpoint to get total students for a given year
@app.get("/total_students/{year}")
def get_total_students(year: int, db: Session = Depends(get_db)):
        res = db.query(models.Class).filter(models.Class.year == year).all()
        if len(res)>0:
            total_students = 0
            for cls in res:
                total_students += cls.count
            return total_students
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Please enter year in correct format")
