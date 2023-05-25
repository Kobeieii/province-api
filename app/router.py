from fastapi import APIRouter
import json

router = APIRouter()

def get_province_json()->dict:
    json_file_path = "./static/province.json" 
    with open(json_file_path, 'r') as j:
        provinces = json.loads(j.read())
    return provinces

@router.get('/provinces', status_code=200)
def provinces():
    provinces = get_province_json()
    province_list = []   
    for prov in provinces.values():
        prov.pop('district')
        province_list.append(prov)
    return province_list

@router.get('/provinces/{id}/district', status_code=200)
def district_of_province(id:int):
    provinces = get_province_json()
    data = provinces.get(str(id))
    if data:
        res = data['district']
        return res
    
@router.get('/provinces/all-data', status_code=200)
def all():
    provinces = get_province_json()
    province_dict = {}
    for data in provinces.values():
        province_dict[data['province']] = data['district']
    return province_dict