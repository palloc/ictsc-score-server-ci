# coding: utf-8

import requests
import json

BASE_URL = 'http://contest.ictsc/api'
EXISITS_ANSWER_ID = '27600'
EXISITS_ANSWER_COMMENT_ID = '276000'


# session
login = {"login": "admin", "password": "admin"}
res = requests.post(BASE_URL+"/session", params=login)
cookie = {'rack.session': res.cookies['rack.session']}

res = requests.get(BASE_URL+'/teams')
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/teams/1')
assert res.status_code == 200
assert json.loads(res.text)

res = requests.get(BASE_URL+'/answers', cookies = cookie)
assert res.status_code == 500#200
res = requests.get(BASE_URL+'/answers/'+EXISITS_ANSWER_ID, cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/answers/'+EXISITS_ANSWER_ID+'/comments/'+EXISITS_ANSWER_COMMENT_ID, cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/issues', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/issues/11200', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/issues/11200/comments', cookies = cookie)
assert res.status_code == 200
#res = requests.get(BASE_URL+'/issues/11200/comments/276000', cookies = cookie)
#assert res.status_code == 200

res = requests.get(BASE_URL+'/problems', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/problems/12', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/problems/12/comments', cookies = cookie)
assert res.status_code == 200
#res = requests.get(BASE_URL+'/problems/12/comments/111', cookies = cookie)
#assert res.status_code == 200

res = requests.get(BASE_URL+'/members', cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/problem_groups', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/problem_groups/1', cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/scores', cookies = cookie)
assert res.status_code == 500
res = requests.get(BASE_URL+'/scores/1', cookies = cookie)
assert res.status_code == 500

res = requests.get(BASE_URL+'/notices', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/notices/1', cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/attachments', cookies = cookie)
assert res.status_code == 200
res = requests.get(BASE_URL+'/attachments/1', cookies = cookie)
assert res.status_code == 404

res = requests.get(BASE_URL+'/notifications', cookies = cookie)
assert res.status_code == 200

res = requests.get(BASE_URL+'/contest', cookies = cookie)
assert res.status_code == 200
