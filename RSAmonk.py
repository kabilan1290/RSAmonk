import os
from sympy import factorint
from Crypto.Util.number import *
intro="figlet -f slant \"RSAmonk\" | lolcat"
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


os.system(intro)
print("--------------------------------------------------")
print("              Author: Game0v3r     ")
print("\n")

prGreen("1.n,p or q,e,c is given - Simple RSA")
prGreen("2.n,e,c is given - Factorization")


a= int(input(""))

def decrypt(p,q,c,n,e)
	phi= (p-1)*(q-1)
	d = inverse(e,phi)
	m = pow(c,d,n)
	flag=(long_to_bytes(m))
	prGreen("Here we go "+str(flag))

if(a==2):
	prGreen("Give me n : ")
	n = int(input(""))
	prGreen("Give me e : ")
	e = int(input(""))
	prGreen("Give me c : ")
	c = int(input(""))
	p,q=factorint(n)
	print("\n")
	decrypt(p,q,c,n,e)

elif(a==1):
	prGreen("Give me n : ")
	n = int(input(""))
	prGreen("Give me p or q : ")
	p = int(input(""))
	prGreen("Give me e : ")
	e = int(input(""))
	prGreen("Give me c : ")
	c = int(input(""))
	print("\n")
	q = n//p
	decrypt(p,q,c,n,e)
