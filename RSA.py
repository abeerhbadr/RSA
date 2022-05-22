import math
import random

def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n # we don’t want −ve integers
    return b

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
            return b
        else:
            return b * a % mod

def ConvertToInt(message_str):
    res = 0
    for i in range(len(message_str)):
        res = res * 256 + ord(message_str[i])
    return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def Encrypt(m, n, e):
    n=int(n)
    e = int(e)
    m_int = ConvertToInt(m)
    #print(ConvertToStr(m_int))
    c = PowMod(m_int, e, n)
    #c = ConvertToStr(c)
    #c = str(c)
    #print(c)
    return c

def Decrypt(c, p, q, e):
    #c = ConvertToInt(c)
    c = int(c)
    #c = int(c)
    p = int(p)
    q = int(q)
    e = int(e)
    phi_n = (p-1)*(q-1)
    d = InvertModulo(e, phi_n)
    m = PowMod(c, d, p*q)
    m = ConvertToStr(m)
    return m

def check_if_prime(n):
    # n is the number to be check whether it is prime or not
    n = int(n)
    # no lets check from 2 to sqrt(n)
    # if we found any facto then we can print as not a prime number
  
    # this flag maintains status whether the n is prime or not
    prime_flag = 0
    if(n > 1):
        for i in range(2, int(math.sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                return not prime_flag
                #break
        if (prime_flag == 0):
            print("prime")
        else:
            print("not prime")
            prime_flag = 1

    else:
        print("not prime")
        prime_flag = 1
    return not prime_flag

def checkCoPrime(e, phin):
    if GCD(e,phin) == 1:
        return True
    else:
        return False

def generatePubKey(phin):
    e = random.randint(1,phin)
    while not checkCoPrime(e, phin):
        e = random.randint(1,phin)
    return e

