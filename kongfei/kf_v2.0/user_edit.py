import random


for i in range(2,901):
    user='admin'+str(i)
    sql = 'insert into mbkf_sys_user (user_id,user_name,user_password,add_date)  values(\'%s\',\'%s\',\'%s\',(select sysdate from dual));'%(user,user,"0a113ef6b61820daa5611c870ed8d5ee")
    print(sql)