import requests
import json

url='https://hackeer-new.firebaseio.com/v0/item/19155826.json'
r=requests.get(url)
print(r.status_code)

#
response_dict=r.json()
with open('new_file.json','w') as f:
    json.dump(response_dict,f,indent=4)