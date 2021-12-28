from factordb.factordb import FactorDB
from Crypto.Util.number import inverse,long_to_bytes
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

prGreen("Give me n :")
n = int(input(""))
prGreen("Give me e :")
e = int(input(""))
prGreen("Give me c :")
c = int(input(""))

f = FactorDB(n)

f.get_factor_list()

f.connect()

p,q = f.get_factor_list()

phi = (p-1)*(q-1)

d = inverse(e,phi)

m = pow(c,d,n)

flag = long_to_bytes(m)

flag = str(flag,"utf-8")

prGreen("Here we go "+flag)