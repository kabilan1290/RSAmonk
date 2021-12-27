import libnum
import math
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
rem = [c1,c2,c3]

mod = [n1,n2,n3]

res=libnum.solve_crt(rem,mod)

#print(res)

val = math.log10(res)/e

#print ("\nLog(res)/e: %d" %val)

val=10**(math.log10(res)/e)


prGreen("\nHere we go!: %s " % long_to_bytes(int(round(val))))

val = round(val)
val = str(val)
prGreen("\nHere we go again!: %s " % bytes.fromhex(val))

#https://medium.com/asecuritysite-when-bob-met-alice/cracking-the-chinese-python-way-89b4e675c63c

