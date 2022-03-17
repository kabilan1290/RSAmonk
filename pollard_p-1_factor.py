from gmpy import gcd
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
prGreen("Give me n :")
n = int(input(">>>"))
def factor(n):
    a = 2
    b = 2
    while True:
        if b % 10000 == 0:
            prGreen("......")
            
        a = pow(a, b, n)
            
        p = gcd(a - 1, n)
        if 1 < p < n:
            prGreen("FOUND " + str(p))
            return p
            
        b += 1

factor(n)