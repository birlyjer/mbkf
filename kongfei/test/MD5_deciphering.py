import hashlib

def deciphering_md5(pwd):
    for i in range(10000000000):
        m = hashlib.md5()
        m.update(str(i).encode("utf-8"))
        if m.hexdigest() == pwd:
            print(i)
            break


pwd = '4297f44b13955235245b2497399d7a93'
deciphering_md5(pwd)


