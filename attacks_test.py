import RSA
import attacks

# generate c,n,e for the attacks
choose_attack = int(input("choose attack -> for mathematical press 1, for CCA press 2 "))
message = input("enter the message: ")

file1 = open('p_q_attacks.txt', 'r')
Lines = file1.readlines()

p_q = []
for line in Lines:
    p_q.append(int(line.strip()))

p = p_q[0]
q = p_q[1]
pubKey = RSA.generatePubKey((p-1)*(q-1))
n = p*q

cipher = RSA.Encrypt(message,n,pubKey)

if choose_attack == 1:
    decipheredtext = attacks.mathematical_attack(cipher,n,pubKey)
    
    with open("MA_results.txt", "a") as a_file:
        a_file.write("Original Message: "+  message+ "\n")
        a_file.write("Deciphered Message: "+  decipheredtext+ "\n")
        a_file.close()

if choose_attack == 2:
    decipheredtext = attacks.CCT_attack(cipher,p,q,pubKey)

    with open("CCT_results.txt", "a") as a_file:
        a_file.write("Original Message: "+  message+ "\n")
        a_file.write("Deciphered Message: "+  decipheredtext+ "\n")
        a_file.close()
