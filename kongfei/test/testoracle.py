# coding=utf-8
from resource.resource import *
from resource.logger import *
import cx_Oracle

db = dbcon('zh01')  # 建立连接
cr = db.cursor()  # 创建游标
# sql = 'select * from ce_inventorymonitor_items'
# cr.execute(sql)
# rs = cr.fetchall()
def rs(sql):
    cr = db.cursor()
    cr.execute(sql)
    result = cr.fetchall()
    return result

num_in1="select packageunitrefname from ce_inventorymonitor_items where nationaldrugcode ='86900941000094'"
num_in2="select usageunitrefname from ce_inventorymonitor_items where nationaldrugcode ='86900941000094'"
num_in3="select packageunitrefname from ce_inventory_in_181220 where nationaldrugcode ='86900941000094'"
cr.execute(num_in1)

rs1 = cr.fetchall()
print(rs1)
cr.execute(num_in2)

rs2 = cr.fetchall()
print(rs2)

cr.execute(num_in3)

rs3 = cr.fetchall()
print(rs3)


if rs1 == rs2:
    in_num = "select sum(drugamount) from ce_inventory_in_181220 where nationaldrugcode='86900941000094'"
    in_num_rs = int(rs(in_num)[0][0])








# if rs1==rs2 :
#     in_num = "select sum(drugamount) from ce_inventory_in_181220 where nationaldrugcode='86900941000094' and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181220),'YYYY-MM-DD hh24:mi:ss')"
#     in_num = rs(in_num)[0][0]
# if rs1==rs3:
#     in_num1 = "select sum(drugamount*(select usageunitamountperpackage from ce_inventorymonitor_items  where  institutioncode=181220 and nationaldrugcode ='86901013000042')) from ce_inventory_in_181220 where nationaldrugcode='86901013000042'  and packageunitrefname in (select packageunitrefname from ce_inventory_in_181220 where nationaldrugcode ='86900144004882' )"
#     in_num2 = "select sum(drugamount) from ce_inventory_in_181220 where nationaldrugcode='86901013000042'  and packageunitrefname not in (select packageunitrefname from ce_inventory_in_181220 where nationaldrugcode ='86900144004882' )"
#     if rs(in_num2) != [(None,)]:
#         in_num = rs(in_num1)[0][0]+rs(in_num2)[0][0]
#     else:
#         in_num = rs(in_num1)[0][0]
# if rs1!=rs3:
#     in_num = "select sum(drugamount) from ce_inventory_in_181220 where nationaldrugcode='86900941000094' and to_char(inputtime,'YYYY-MM-DD hh24:mi:ss')>=to_char((select max(checktime) from CE_INVENT_REG where institutioncode=181220),'YYYY-MM-DD hh24:mi:ss')"
#     in_num = rs(in_num)[0][0]
#
# print(in_num)




