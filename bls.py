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
'CXUEDUCATNLB0902M','CXUEDUCATNLB0903M','CXUEDUCATNLB0904M',
'CXUEDUCATNLB0905M','CXUEDUCATNLB1002M','CXUEDUCATNLB1003M',
'CXUEDUCATNLB1004M','CXUEDUCATNLB1005M', 'CXUEDUCATNLB1102M', 
'CXUEDUCATNLB1103M', 'CXUEDUCATNLB1104M', 'CXUEDUCATNLB1105M', 
'CXUEDUCATNLB1302M', 'CXUEDUCATNLB1303M', 'CXUEDUCATNLB1304M', 
'CXUEDUCATNLB1305M', 'CXUEDUCATNLB1306M', 'CXUEDUCATNLB1307M', 
'CXUEDUCATNLB1308M', 'CXUEDUCATNLB1309M'],"startyear":"2000", "endyear":"2017","registrationkey":r_key})
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)
json_data = json.loads(p.text)
#print(json.dumps(json_data,indent=4))
for series in json_data['Results']['series']:
#    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesid_list=[]
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['periodName']
        value = item['value']
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        education_list.append({"series id":seriesId,
        "year":year,
        "period name":period,
        "value":value,
        "footnote":footnotes})
        seriesid_list.append({"series id":seriesId,
        "year":year,
        "period name":period,
        "value":value,
        "footnote":footnotes})
    seriesid_df=pd.DataFrame(seriesid_list)
    seriesid_df=seriesid_df[["series id","year","period name","value"]]
    seriesid_df.to_csv(out_path + seriesId +'.csv ',index=False,header=True)
education_df=pd.DataFrame(education_list) 
education_df=education_df[["series id","year","period name","value"]]
education_df.to_csv(csv_out,index=False,header=True)       
  #      if 'M01' <= period <= 'M12':
    #    x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    # output = open(seriesId + '.txt','w')
    # output.write (x.get_string())
    # output.close()
