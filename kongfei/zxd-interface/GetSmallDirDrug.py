#coding=utf-8

import requests
import json
import re
from resource.resource import *
import logging,time,sys


logger = logging.getLogger("Appname")#获取logger对象
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')#设置格式
file_handler = logging.FileHandler("test512.log")
file_handler.setFormatter(formatter)#指定输出格式
# 控制台日志
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter  # 也可以直接给formatter赋值
# 为logger添加的日志处理器
logger.addHandler(file_handler)
logger.addHandler(console_handler)

# 指定日志的最低输出级别，默认为WARN级别
logger.setLevel(logging.INFO)


#药品小目录获取
data ={'nousercheck':1,'eventcode':'GetSmallDirDrug','funid':'sysevent','RequestDate':'20171205105516',
        'RequestId':'20171205105516165181220_HIS01_HIS01RQ000007','trancode':70,'trancode':"V1.0",
       'data':json.dumps({"DistrictCode": "510181","InstituteID": "181220"})}

try:
    r = requests.post(test_url_z,data=data,timeout=10)


    t=r.text

    tt=t.replace('success',"\"success\"")
    tt=tt.replace('true',"\"true\"")
    tt=tt.replace('data',"\"data\"")
    tt=tt.replace('message',"\"message\"")
    re=eval(tt)



    print(re['data']['ProcessInfo'])

except requests.exceptions.ReadTimeout:
    logger.error('Timeout')



