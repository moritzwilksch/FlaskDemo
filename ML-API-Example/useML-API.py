
# %%
import requests
import json

url = "http://127.0.0.1:5000/api/getsquare"
# explicit specification of JSON in header is necessary
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

result = requests.post(url, json.dumps({"inputnum": 12}), headers=headers)
print(result.json())