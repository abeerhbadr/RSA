import RSA
import random

# Brute Force (Mathematical Attack) 
def mathematical_attack(c, n, e):
    p = 0
    q = 0
    decipheredtext = ''
    for num in range(2, int((n**0.5)+1)):
        if n%num == 0:
            p = num
            q = n // num
            decipheredtext = RSA.Decrypt(c, p, q, e)
            return decipheredtext
    return decipheredtext

#Chosen Cipher Text Attack
def CCT_attack(c, p, q, e):
    n = p*q
    r = random.randint(1,n)
    while not RSA.checkCoPrime(r, n):
        r = random.randint(1,n)
    cc = RSA.PowMod(c,1,n) * RSA.PowMod(r,e,n)
    y = RSA.Decrypt(cc,p,q,e)
    m = RSA.PowMod(RSA.ConvertToInt(y) * RSA.InvertModulo(r,n), 1, n)
    m = RSA.ConvertToStr(m)
    return m