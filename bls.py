import requests
import json
import prettytable
from config import r_key 
#headers = {'Content-type': 'application/json'}
#data = json.dumps({"seriesid": ['CUUR0000SA0','SUUR0000SA0'],"startyear":"2011", "endyear":"2014","registrationkey=":r_key})
#p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/', data=data, headers=headers)

series_id="CXUEDUCATNLB1402"
p = requests.post('https://api.bls.gov/publicAPI/v2/timeseries/data/'+ series_id + "?"+ r_key)
# for downloading the consumer expenditure survey
#p = requests.post('https://api.bls.gov/publicAPI/v2/surveys/' + 'CX'+"?" + r_key)
json_data = json.loads(p.text)
print(json.dumps(json_data,indent=4))
for series in json_data['Results']['series']:
    x=prettytable.PrettyTable(["series id","year","period","value","footnotes"])
    seriesId = series['seriesID']
    for item in series['data']:
        year = item['year']
        period = item['period']
        value = item['value']
        print(value)
        footnotes=""
        for footnote in item['footnotes']:
            if footnote:
                footnotes = footnotes + footnote['text'] + ','
        if 'M01' <= period <= 'M12':
            x.add_row([seriesId,year,period,value,footnotes[0:-1]])
    output = open(seriesId + '.txt','w')
    output.write (x.get_string())
    output.close()
   