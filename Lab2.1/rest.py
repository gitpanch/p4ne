import requests, json, pprint

host_ip = '10.31.70.210'
login = 'restapi'
password = 'j0sg1280-7@'
host_url = 'https://' + host_ip + ':55443'

r = requests.post(host_url + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(host_url + '/api/v1/interfaces', headers=header, verify=False)
pprint.pprint(r.json())

list = []
for i in r.json()['items']:
    list.append(i['if-name'])

for l in list:
    url = host_url +  '/api/v1/interfaces/' + l + '/statistics'
    r = requests.get(url, headers=header, verify=False)
    print('In packets: ', r.json()['in-total-packets'], 'out packets: ', r.json()['out-total-packets'])









