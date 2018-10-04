import requests
import json
import prettytable
import numpy as np
import pandas as pd
from config import r_key 
csv_out='output/education_data.csv'
out_path='output/'
headers = {'Content-type': 'application/json'}
education_list=[]
data = json.dumps({"seriesid": ['CXUEDUCATNLB0806M','CXUEDUCATNLB0807M','CXUEDUCATNLB0808M','CXUEDUCATNLB0809M',
'CXUEDUCATNLB1002M','CXUEDUCATNLB1003M',
'CXUEDUCATNLB1004M','CXUEDUCATNLB1005M', 'CXUEDUCATNLB1102M', 
'CXUEDUCATNLB1103M', 'CXUEDUCATNLB1104M', 'CXUEDUCATNLB1105M', 
'CXUEDUCATNLB1302M', 'CXUEDUCATNLB1303M', 'CXUEDUCATNLB1304M', 
'CXUEDUCATNLB1305M', 'CXUEDUCATNLB1306M', 'CXUEDUCATNLB1307M', 
'CXUEDUCATNLB1308M', 'CXUEDUCATNLB1309M'],"startyear":"2000", "endyear":"2017","registrationkey":r_key})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
#print(json.dumps(json_data,indent=4))
titles={'CXUEDUCATNLB0806M':'area_urban',
 'CXUEDUCATNLB0807M':'area_urban_central_city',
 'CXUEDUCATNLB0808M':'area_urban_other',
 'CXUEDUCATNLB0809M':'area_rural',
 'CXUEDUCATNLB1002M':'origin_hispanic_latino',
 'CXUEDUCATNLB1003M':'origin_not_hispanic_latino',
 'CXUEDUCATNLB1004M':'not_hispanic_white_other',
 'CXUEDUCATNLB1005M':'not_hispanic_black_african-american', 
 'CXUEDUCATNLB1102M':'region_northeast', 
 'CXUEDUCATNLB1103M':'region_midwest', 
 'CXUEDUCATNLB1104M':'region_south', 
 'CXUEDUCATNLB1105M':'region_west', 
 'CXUEDUCATNLB1302M':'ed_total_less_than_college_graduate', 
 'CXUEDUCATNLB1303M':'ed_less_than_highschool_graduate', 
 'CXUEDUCATNLB1304M':'ed_highschool_graduate', 
 'CXUEDUCATNLB1305M':'ed_highschool_graduate_some_college',
 'CXUEDUCATNLB1306M':'ed_associate_degree',
 'CXUEDUCATNLB1307M':'ed_total_college_graduate', 
 'CXUEDUCATNLB1308M':'ed_bachelor_degree', 
 'CXUEDUCATNLB1309M':'ed_master_professional_doctorate'}

education_list=[]
for series in json_data['Results']['series']:
#    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesid_list=[]
    seriesId = series['seriesID']
    if 'LB08' in seriesId:
        group = 1
    elif 'LB10' in seriesId:
        group =2
    elif 'LB11' in seriesId:
        group =3
    else:
        group = 4
    for item in series['data']:
        year = item['year']
        value = item['value']        
        education_list.append({"grouping":titles[seriesId],
                               "group":group,
                               "year":year,
                               "value":value})
        seriesid_list.append({"grouping":titles[seriesId],
                              "group":group,
                              "year":year,
                              "value":value})
    seriesid_df=pd.DataFrame(seriesid_list)
    seriesid_df=seriesid_df[["grouping","group","year","value"]]
    seriesid_df.to_csv(out_path + seriesId +'.csv ',index=False,header=True)
education_df=pd.DataFrame(education_list) 
education_df=education_df[["grouping","group","year","value"]]
education_df.to_csv(csv_out,index=False,header=True)       

