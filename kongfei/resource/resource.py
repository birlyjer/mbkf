#coding=utf-8
import cx_Oracle
test_url_z = 'http://192.168.0.100:8080/KMY/fileAction.do'#中心端接口


test_url_z_gw = 'http://183.62.74.187:8139/KMY/fileAction.do'


login_url='http://192.168.0.100:8080/welcome/rest/system/user_id/login'

login_url_ui='http://192.168.0.100:8080/welcome'


#连接数据库
def dbcon(name):
    if name=='zh01':
        db = cx_Oracle.connect('zh01/123456@192.168.0.100/kmy')
        return db

#返回查询结果
def rs(sql):
    cr = dbcon.db.cursor()
    cr.execute(sql)
    rs = cr.fetchall()
    return rs


