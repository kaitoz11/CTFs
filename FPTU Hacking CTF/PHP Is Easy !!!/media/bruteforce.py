import hashlib
import re

prefix = '0e'


def breakit():
    i = 0
    while 1:
        s = prefix + str(i)
        hashed_s = hashlib.md5(s.encode()).hexdigest()
        i+=1
        r = re.match('^0e[0-9]{30}', hashed_s)
        if r:
            print("[+] found! md5( {} ) ---> {}".format(s, hashed_s))
            print("[+] in {} iterations".format(i))
            exit(0)

        if i % 1000000 == 0:
            print("[+] current value: {}       {} iterations, continue...".format(s, i))

breakit()