from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config import SessionLocal, engine
import schemas
from controller import (
    get_provinces,
    get_districts,
    get_subdistricts,
    format_district_n_subdistrict
)
from exceptions import InvalidId
import json
from typing import List

router = APIRouter()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get('/provinces', response_model=List[schemas.Province], status_code=200)
def provinces(db: Session = Depends(get_db)):
    return get_provinces(db)

@router.get('/provinces/{province_id}/district', response_model=List[schemas.District], status_code=200)
def district_of_province(province_id:int, db: Session = Depends(get_db)):
    try:
        return get_districts(province_id, db)
    except InvalidId:
        raise HTTPException(status_code=404, detail="Invalid province id")

@router.get('/provinces/{province_id}/districts/subdistricts', response_model=List[schemas.ResponseDistNSubDist], status_code=200)
def subdistrict_and_district_of_province(province_id:int, db: Session = Depends(get_db)):
    try:
        districts = get_districts(province_id, db)
        res = format_district_n_subdistrict(districts)
        return res
    except InvalidId:
        raise HTTPException(status_code=404, detail="Invalid province id")
    
@router.get('/districts/{district_id}/subdistrict', response_model=List[schemas.Subdistrict], status_code=200)
def subdistrict_of_district(district_id:int, db: Session = Depends(get_db)):
    try:
        return get_subdistricts(district_id, db)
    except:
        raise HTTPException(status_code=404, detail="Invalid district id")