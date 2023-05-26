from sqlalchemy.orm import Session
import models
import schemas
from exceptions import InvalidId

def get_provinces(db: Session):
    return db.query(models.Province).all()

def get_districts(province_id:int, db: Session):
    province = db.query(models.Province).filter(models.Province.id == province_id).first()
    if not province:
        raise InvalidId
    return province.district

def get_subdistricts(district_id:int, db: Session):
    district = db.query(models.District).filter(models.District.id == district_id).first()
    if not district:
        raise InvalidId
    return district.subdistrict