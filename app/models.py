from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from config import Base

class Province(Base):
    __tablename__ = 'province'

    id = Column(Integer, primary_key=True)
    name_th = Column(String, unique=True)
    name_en = Column(String, unique=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)

    district = relationship("District", back_populates="province")

class District(Base):
    __tablename__ = 'district'

    id = Column(Integer, primary_key=True)
    name_th = Column(String)
    name_en = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    province_id = Column(Integer, ForeignKey('province.id'))

    province = relationship("Province", back_populates="district")
    subdistrict = relationship("Subdistrict", back_populates="district")

class Subdistrict(Base):
    __tablename__ = 'subdistrict'

    id = Column(Integer, primary_key=True)
    name_th = Column(String)
    name_en = Column(String)
    zip_code = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now())
    deleted_at = Column(DateTime, nullable=True)
    amphure_id = Column(Integer, ForeignKey('district.id'))

    district = relationship("District", back_populates="subdistrict")
