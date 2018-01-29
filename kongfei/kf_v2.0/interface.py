import requests
from resource.resource import *
from resource.logger import *
import json
import time

login_data={'USER_ID':'admin100','USER_PASSWORD':'888'}
login_url=login_url.replace('user_id',login_data['USER_ID']) #动态url
r = requests.post(login_url,login_data)



url='http://192.168.0.100:8080/welcome/rest/user/list?pageSize=200&pageNo=2&USER_ID=&orderBy=ADD_DATE%40desc&_=1515480072073'

rr= requests.get(url,cookies=r.cookies)
# print(rr.text)
re = rr.text
re=eval(re)
print(url)
print(re['rows'][0:30])

print('\n')
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())))
time.sleep(1)

url1='http://192.168.0.100:8080/welcome/rest/user/list?pageSize=200&pageNo=3&USER_ID=&orderBy=ADD_DATE%40desc&_=1515480072074'

rrr= requests.get(url1,cookies=r.cookies)


print(url1)

rre = rrr.text
rre=eval(rre)
print(rre['rows'][0:30])
