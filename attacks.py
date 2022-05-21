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
def CCT_attack(c, n, e):
    r = random.randint(1,n)
    while not RSA.checkCoPrime(e, n):
        e = random.randint(1,n)
    cc = c * RSA.PowMod(r,e,n)

    y = RSA.Decrypt(cc,)

    return 1
