from Crypto.Util.number import *
from gmpy2 import *

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prGreen("Give me n :")
n = int(input(">>>"))
prGreen("Give me ct :")
ct = int(input(">>>"))
prGreen("Give me pad_length :")
padding_length = int(input(">>>"))
e = 3

new_ct = ct * pow(inverse(256, n) ** padding_length, e, n)
new_ct %= n

prGreen(long_to_bytes(iroot(new_ct,3)[0]))