# coding: utf-8

import requests
import json

BASE_URL = 'http://contest.ictsc/api'

# session
login = {"login": "cocoa", "password": "cocoa"}
res = requests.post(BASE_URL+"/session", params=login)
cookies = {'rac.session': res.cookies['rack.session']}

res = requests.get(BASE_URL+'/teams')
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/teams/1')
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/answers', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/answers/27600/comments', cookies = cookie)
print res.text
assert res.status_code == 200

res = requests.get(BASE_URL+'/answers/27600/comments/276000', cookies = cookie)
print res.status_code
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/issues', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/issues/11200/cmments', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/issues/comments/276000', cookies = cookie)
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/problems', cookies = cookie)
print res.text
assert res.status_code == 200
assert json.loads(res.text)
