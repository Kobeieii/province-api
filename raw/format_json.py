import pandas as pd
import json

df_province = pd.read_json('./all-province.json')
df_district = pd.read_json('./all-district.json')

print('province shape: ', df_province.shape)
print('district shape: ', df_district.shape)

df_res = df_province.merge(df_district, left_on='id', right_on='province_id', suffixes=('_p', '_d'))[['id_p','name_th_p','name_th_d']]
df_res = df_res.rename(columns={'id_p':'id', 'name_th_p':'province', 'name_th_d':'district'})
print('result shape: ', df_res.shape)

res = df_res.groupby(['id','province'])['district'].apply(list).reset_index().to_dict('records')

province_dict = {}
for province in res:
    id = province.get('id')
    province_dict[id] = province

path = '../app/static/province.json'
with open(path, "w", encoding='utf8') as outfile:
    outfile.write(json.dumps(province_dict, indent=4, ensure_ascii=False))