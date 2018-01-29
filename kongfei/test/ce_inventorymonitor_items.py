#coding=utf-8
from resource.resource import *
from resource.logger import *
import cx_Oracle

db = dbcon('zh01')  # 建立连接
cr = db.cursor()  # 创建游标
# monitor_181160= "select nationaldrugcode,genericname  from ce_inventorymonitor_items where institutioncode=181160"
#
# cr.execute(monitor_181160)
# rs = cr.fetchall()
# print(rs)
drug_code = [ '86902122000015']
in_num = "select sum(drugamount*packageproportion) from ce_inventory_in_181160 where nationaldrugcode='86902122000015' and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181160),'YYYY-MM-DD hh24:mi:ss')"

cr.execute(in_num)
rs = cr.fetchall()
if rs == [(None,)]:
    in_num_int = 0
else:
    in_num_int = int(rs[0][0])

print(in_num_int)


