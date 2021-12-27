import os
from sympy import *
from gmpy2 import *
from Crypto.Util.number import *
intro="figlet -f slant \"RSAmonk\" | lolcat"
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))


os.system(intro)
print("--------------------------------------------------")
print("              Author: Game0v3r     ")
print("\n")

prGreen("1.n,p or q,e,c is given - Simple RSA")
prGreen("2.n,e,c is given - Factorization")
prGreen("3.e=3,n,c is given - Cube-Root Attack")
prGreen("4.Factorization for Sexy,Cousin and Twin primes")
prGreen("5.n,d,e is given - Algorthmic factorization") #https://www.di-mgt.com.au/rsa_factorize_n.html
prGreen("6.n1,n2,n3,c1,c2,c3,e=3 - Hastad Broadcast attack")

a= int(input(""))

def decrypt(p,q,c,n,e):
	phi= (p-1)*(q-1)
	d = inverse(e,phi)
	m = pow(c,d,n)
	flag=(long_to_bytes(m))
	prGreen("Here we go "+str(flag,'utf-8'))

def algofactor(n,e,d):
	k=d*e-1
	t = k
	primes = [2,3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
	prime_length = len(primes)
	for i in range(0,prime_length):
		while(t%2==0):
			t = t/2
			g = prime_length[i]
			x = g**t % n 
			x = x.rstrip("L")
			if(x!=1):
				print(x)
				exit()
			else:
				continue



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
elif(a==3):
	prGreen("Give me c : ")
	c = int(input(""))
	e=3
	m = iroot(c,e)
	flag=(long_to_bytes(m[0]))
	prGreen("Here we go : "+str(flag,'utf-8'))
elif(a==4):
	prGreen("1.SexyPrime - Differs by six")
	prGreen("2.CousinPrime - Differs by four")
	prGreen("3.TwinPrime - Differs by two")
	x = symbols('x')
	b = int(input(""))
	if(b==1):
		prGreen("Give me n :")
		n = int(input(""))
		expr = x*(x+6)-n
		m=solve(expr)
		prGreen("The factors of "+str(n)+" are "+str(m[0])+" and "+str(m[1]))
	elif(b==2):
		prGreen("Give me n :")
		n = int(input(""))
		expr = x*(x+4)-n
		m=solve(expr)
		prGreen(m)
		prGreen("The factors of "+str(n)+" are "+str(m[0])+" and "+str(m[1]))


	else:
		prGreen("Give me n :")
		n = int(input(""))
		expr = x*(x+2)-n
		m=solve(expr)
		prGreen(m)
		prGreen("The factors of "+str(n)+" are "+str(m[0])+" and "+str(m[1]))

elif(a==5):
	os.system("python algofactor.py")
elif(a==6):
	os.system("python3 crt.py")
