def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

#https://www.di-mgt.com.au/rsa_factorize_n.html

def gcd(x, y):
  
   while(y):
       x, y = y, x % y
  
   return x
def failFunction():
	print("Prime factors not found")

def outputPrimes(a, n):
	p = gcd(a, n)
	q = int(n // p)
	if p > q:
		p, q = q, p
	print("Found factors p and q")
	print("p = {0}".format(str(p)))
	print("q = {0}".format(str(q)))
	return p,q


def RecoverPrimeFactors(n, e, d):

	k = d * e - 1
	if k % 2 == 1:
		failFunction()
		return 0, 0
	else:
		t = 0
		r = k
		while(r % 2 == 0):
			r = int(r // 2)
			t += 1
		for i in range(1, 101):
			g = random.randint(0, n) # random g in [0, n-1]
			y = pow(g, r, n)
			if y == 1 or y == n - 1:
				continue
			else:
				for j in range(1, t): # j \in [1, t-1]
					x = pow(y, 2, n)
					if x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q
					elif x == n - 1:
						continue
					y = x
					x = pow(y, 2, n)
					if  x == 1:
						p, q = outputPrimes(y - 1, n)
						return p, q




prGreen("Give me n :")
n = int(input("   "))
prGreen("Give me e :")
e = int(input("   "))
prGreen("Give me d :")
d = int(input("   "))


RecoverPrimeFactors(n,e,d)
