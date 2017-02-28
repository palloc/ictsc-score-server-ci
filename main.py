# coding: utf-8

import requests
import json

BASE_URL = 'http://stg.ictsc.pref.yokohama'

res = requests.get(BASE_URL+'/api/teams')
assert res.status_code == 200
assert json.loads(res.text)

res = requests.post(BASE_URL+'/api/teams')
assert res.status_code == 403


res = requests.get(BASE_URL+'/api/teams/1')
assert res.status_code == 200
assert json.loads(res.text)

# 権限フィルタ
res = requests.put(BASE_URL+'/api/teams/1')
assert res.status_code == 404

res = requests.patch(BASE_URL+'/api/teams/1')
assert res.status_code == 404

res = requests.delete(BASE_URL+'/api/teams/1')
assert res.status_code == 404


# session
sess = 'BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiRWY3MGIxODUzMjI2ZTdmZmJkMjYz%0AZjQzOTg0YzAyYWU3OTcwMjJiMDlhOTIzZTY5YzljNmYwMDllZmRmODI2YzMG%0AOwBGSSIObWVtYmVyX2lkBjsARmkW%0A--1500cac8d9f5e1df7a480ea66117ed0c098ffe2d'
cookie = {'rack.session': sess}

res = requests.get(BASE_URL+'/api/answers', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/api/answers/27600/comments', cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/api/answers/27600/comments/276000', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/api/issues', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/api/issues/11200/cmments', cookies = cookie)
print res.text
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/api/issues/comments/276000', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)
