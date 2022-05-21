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
    r = random.randint(1,n)
    while not RSA.checkCoPrime(r, n):
        r = random.randint(1,n)
    cc = RSA.PowMod(c,1,n) * RSA.PowMod(r,e,n)
    y = RSA.Decrypt(cc,p,q,e)
    m = RSA.PowMod(RSA.ConvertToInt(y) * RSA.InvertModulo(r,n), 1, n)
    m = RSA.ConvertToStr(m)
    return m

# generate c,n,e for the attacks
choose_attack = input("choose attack -> for mathematical press 1, for CCA press 2 ")
message = input("enter the message: ")

file1 = open('p_q_attacks.txt', 'r')
Lines = file1.readlines()

pandq = []
for line in Lines:
    pandq.append(int(line.strip()))

p = pandq[0]
q = pandq[1]
pubKey = RSA.generatePubKey((p-1)*(q-1))
n = p*q

cipher = RSA.Encrypt(message,n,pubKey)

if choose_attack == str(1):
    decipheredtext = mathematical_attack(cipher,n,pubKey)
    
    with open("MA_results", "a") as a_file:
        a_file.write("Original Message: "+  message+ "\n")
        a_file.write("Deciphered Message: "+  decipheredtext+ "\n")
        a_file.close()

if choose_attack == str(2):
    decipheredtext = CCT_attack(cipher,p,q,pubKey)

    with open("CCT_results", "a") as a_file:
        a_file.write("Original Message: "+  message+ "\n")
        a_file.write("Deciphered Message: "+  decipheredtext+ "\n")
        a_file.close()



