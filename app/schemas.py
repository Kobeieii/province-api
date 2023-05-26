from pydantic import BaseModel

class Province(BaseModel):
    id: int
    name_th: str
    name_en: str

    class Config:
        orm_mode = True

class District(BaseModel):
    id: int
    name_th: str
    name_en: str

    class Config:
        orm_mode = True

class Subdistrict(BaseModel):
    id: int
    name_th: str
    name_en: str
    zip_code: str

    class Config:
        orm_mode = True

class ResponseDistNSubDist(BaseModel):
    district: District
    subdistrict: list[Subdistrict]

    class Config:
        orm_mode = True