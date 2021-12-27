def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

#https://www.di-mgt.com.au/rsa_factorize_n.html

def computeGCD(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x

def algofactor(n,e,d):
	k=d*e-1
	t = k
	primes = ["2","3", "5", "7", "11", "13", "17", "19", "23", "29", "31", "37"]
	prime_length = len(primes)
	i =0
	while (i <= prime_length):
		while(t%2==0):
			t = t/2
			g = primes[i]
			g = int(g)
			x = pow(g,t,n)
			
			x = str(x).rstrip("L")
			if(x!="1"):
				x = int(x)
				
				y = computeGCD(x-1,n)
				if(y!=1):
					p=y
					q=n/p
					prGreen("The value of p is "+str(p))
					prGreen("The value of q is "+str(q))
					exit()
				else:
					continue
			else:
				i =i+1
				continue

prGreen("Give me n :")
n = int(input("   "))
prGreen("Give me e :")
e = int(input("   "))
prGreen("Give me d :")
d = int(input("   "))


algofactor(n,e,d)