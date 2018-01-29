#coding=utf-8

def login(x):
    username = '//*[@id="USER_ID"]'

    pwd = '//*[@id="USER_PASSWORD"]'

    submit = '//*[@id="login"]'
    s=['username','pwd','submit']
    ss=[username,pwd,submit]
    d = dict(zip(s,ss))

    if x in s  :
        return d[x]




def jxcgl(x):
    jxcgl = '/ html / body / div[2] / div[2] / nav[1] / div[2] / div[1] / ul / li[2] / a / span[1]'
    jxc_rs='/html/body/div[2]/div[2]/nav[1]/div[2]/div[1]/ul/li[2]/ul/li[1]'
    drugin='/html/body/div[2]/div[2]/nav[1]/div[2]/div[1]/ul/li[2]/ul/li[2]'
    drugout='/html/body/div[2]/div[2]/nav[1]/div[2]/div[1]/ul/li[2]/ul/li[3]'




    s = ['jxcgl','jxc_rs','drugin','drugout']
    ss = [jxcgl,jxc_rs,drugin,drugout]
    d = dict(zip(s, ss))

    if x in s:
        return d[x]
# def login():
#
#     username = '//*[@id="USER_ID"]'
#     pwd = '//*[@id="USER_PASSWORD"]'
#
#     submit = '//*[@id="login"]'



