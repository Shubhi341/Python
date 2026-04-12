import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

# print(response.json())
complete_detail=response.json()

# print(complete_detail[0]["user"]["login"])

for element in range(len(complete_detail)):
    print(complete_detail[element]["user"]["login"])
