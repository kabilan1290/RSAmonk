from Crypto.Util.number import long_to_bytes,inverse
#dp=d%(p-1)
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

prGreen("Give me n :")
n = int(input(""))
prGreen("Give me e :")
e = int(input(""))
prGreen("Give me c :")
ct = int(input(""))
prGreen("Give me dp :")
dp = int(input(""))


for k in range(1,e):
	p = (e*dp-1+k)//k
	if n % p == 0:
		q = n//p
		phi = (p-1)*(q-1)
		d = inverse(e,phi)

		m = pow(ct,d,n)
		prGreen("Here we go :")
		prGreen(str(long_to_bytes(m),'utf-8'))