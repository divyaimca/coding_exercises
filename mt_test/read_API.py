import requests
import json
import copy
url = "https://mobile2.successfactors.com/app_info"

resp = requests.get(url)

json_response = resp.json()



json_copy = copy.deepcopy(json_response)

print(json_copy[0])


for item in json_copy:
    #print(item)
    # for k,v in item.items():
    #     if k == "MP":
    json_copy[0]["MP"] = json_copy[3]["FILE"]

print(json_copy[0])
print(json_response[0])

