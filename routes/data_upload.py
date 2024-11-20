from fastapi import APIRouter, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
import pandas as pd
from db.database import get_db
from db.models import Department, Job, HiredEmployee
from datetime import datetime

# router to manage the routes of loading data
router = APIRouter()

@router.post("/upload/departments")
async def upload_departments(file: UploadFile, db: Session = Depends(get_db)):
    try:
        # as csv files have not headers we need to ssign it
        df = pd.read_csv(file.file, header=None, names=["id", "department"])
        
        print(df.head())

        # intert each row in the db
        for _, row in df.iterrows():
            db.add(Department(id=row['id'], department=row['department']))
        db.commit()
        return {"status": "Departments uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading data: {e}")

@router.post("/upload/jobs")
async def upload_jobs(file: UploadFile, db: Session = Depends(get_db)):
    try:

        df = pd.read_csv(file.file, header=None, names=["id", "job"])
        
        for _, row in df.iterrows():
            db.add(Job(id=row['id'], job=row['job']))
        db.commit()
        return {"status": "Jobs uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading data: {e}")

@router.post("/upload/hired_employees")
async def upload_hired_employees(file: UploadFile, db: Session = Depends(get_db)):
    try:
        df = pd.read_csv(file.file, header=None, names=["id", "name", "datetime", "department_id", "job_id"])
        
        df['datetime'] = pd.to_datetime(df['datetime'], format='%Y-%m-%dT%H:%M:%SZ', errors='coerce')

        for _, row in df.iterrows():
            # as we are working in python we need to manage the datetimes format
            datetime_value = row['datetime'].to_pydatetime() if pd.notna(row['datetime']) else None
            db.add(HiredEmployee(
                id=row['id'],
                name=row['name'],
                datetime=datetime_value,  # if conversion fails then None
                department_id=int(row['department_id']) if pd.notna(row['department_id']) else None,
                job_id=int(row['job_id']) if pd.notna(row['job_id']) else None
            ))
        db.commit()
        return {"status": "Hired Employees uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error uploading data: {e}")
