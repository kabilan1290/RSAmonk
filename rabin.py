from Crypto.Util.number import long_to_bytes
from sympy import factorint
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

e =2
prGreen("Give me ct :")
c = int(input(">>>"))
prGreen("Give me n :")
n = int(input(">>"))

p,q =factorint(n)
phi = (p-1)*(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

g ,yp, yq = egcd(p,q)
mp = pow(c,(p+1)/4,p)
mq = pow(c,(q+1)/4,q)



r = (yp*p*mq + yq*q*mp) % n
mr = n - r
s = (yp*p*mq - yq*q*mp) % n
ms = n - s
for num in [r,mr,s,ms]:
    prGreen(long_to_bytes(num))