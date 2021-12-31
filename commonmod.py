from gmpy2 import  *
from Crypto.Util.number import *
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

prGreen("Give me e1 :")
e1 = int(input(" "))
prGreen("Give me e2 :")
e2 = int(input(" "))
prGreen("Give me c1 :")
c1 = int(input(" "))
prGreen("Give me c2 :")
c2 = int(input(" "))
prGreen("Give me n :")
N = int(input(" "))

try:
	assert (gcd(e1,e2)==1)
	g, s1, s2 = gmpy2.gcdext(e1, e2)
	if(s1<0):
		c1inversed = gmpy2.invert(c1, N)
		m1 = pow(c1inversed,-s1,N)

		m2 = pow(c2,s2,N)
		final = (m1 *m2)%N
		prGreen("Here we go")
		prGreen(long_to_bytes(final))
	else:
		c2inversed = gmpy2.invert(c2,N)
		m1 = pow(c2inversed,-s2,N)

		m2 = pow(c1,s1,N)
		final = (m1 *m2)%N
		prGreen("Here we go")
		prGreen(long_to_bytes(final))

except:
	prGreen("oops! Gcd(e1,e2) is not equal to 1")


