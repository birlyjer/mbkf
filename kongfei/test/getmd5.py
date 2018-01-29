import hashlib
#输入要加密的字符串，输出md5加密后的字符串
def md5(str):
    m = hashlib.md5()
    m.update(str.encode("utf-8"))
    return(m.hexdigest())
