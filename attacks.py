import RSA

def MathematicalAttack(c, n, e):
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