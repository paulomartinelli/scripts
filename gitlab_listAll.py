import requests
import math

urlRepo = "https://XXXXX/gitlab"
api = "/api/v4/projects?private_token="
token = "XXXXXXXX"
url = urlRepo + api + token

r = requests.get(url)
h = r.headers

pp = int(h['X-Per-Page'])
total = int(h['X-Total'])
lastPage = math.ceil(total/pp)
sistemas = []

for x in range(1, lastPage+1):
    urlTemp = url + '&page=' +str(x)
    r = requests.get(urlTemp)
    data = r.json()
    for a in data:
        sistemas.append(a['web_url'])

sistemas.sort()
for b in sistemas:
    print('git clone ' + b + '.git')
