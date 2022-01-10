from Crypto.Util.number import bytes_to_long, isPrime,inverse,long_to_bytes


def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

prGreen("Give me c")
c = int(input(">>>"))
prGreen("Give me e")
e = int(input(">>>"))
prGreen("Give me dp")
dp = int(input(">>>"))
prGreen("Give me dq")
dq = int(input(">>>"))

for kq in range(1, e):
	q_mul = dq * e - 1
	if q_mul % kq == 0:
		q1 = (q_mul // kq) + 1
		if isPrime(q1):
			prGreen("Potential q: " + str(q1))
			q=q1


for kp in range(1, e):
	p_mul = dp * e - 1
	if p_mul % kp == 0:
		p1 = (p_mul // kp) + 1
		if isPrime(p1):
			prGreen("Potential p: " + str(p1))
			p = p1


phi =(p-1)*(q-1)

n =p*q
d = inverse(e,phi)

m =pow(c,d,n)
print("\n")
prGreen(long_to_bytes(m))