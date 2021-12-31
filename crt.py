from sympy import root
from sympy.ntheory.modular import crt
from Crypto.Util.number import *
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prGreen("Give me n1 :")
n1 = int(input(""))
prGreen("Give me n2 :")
n2 = int(input(""))
prGreen("Give me n3 :")
n3 = int(input(""))
prGreen("Give me c1 :")
c1 = int(input(""))
prGreen("Give me c2 :")
c2 = int(input(""))
prGreen("Give me c3 :")
c3 = int(input(""))
e=3

m=int(root(crt([n1,n2,n3],[c1,c2,c3])[0],3))


prGreen("\nHere we go!: %s " % long_to_bytes(m))

#val = round(val)
#val = str(val)
#prGreen("\nHere we go again!: %s " % bytes.fromhex(val))

#https://medium.com/asecuritysite-when-bob-met-alice/cracking-the-chinese-python-way-89b4e675c63c

