import socket
import RSA
import sympy 

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)  #changed it from 65432 to 65433 bec it gave an error

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()

    p = 0
    q = 0
    p_input = input("enter p: ")
    q_input = input("enter q: ")
    if p_input and q_input:
        while p_input and q_input:
            #if(RSA.check_if_prime(p_input) and RSA.check_if_prime(q_input)):
            if(sympy.isprime(int(p_input)) and sympy.isprime(int(q_input))):
                p = int(p_input)
                q = int(q_input)
                break
            else:
                print("enter prime numbers")
                p_input = input("enter p: ")
                q_input = input("enter q: ")
    else:
        file1 = open('p_q.txt', 'r')
        Lines = file1.readlines()
        p_q = []
        for line in Lines:
            p_q.append(int(line.strip()))
        p = p_q[0]
        q = p_q[1]

    e_input = input("enter e: ")
    if e_input:
        pubKey = int(e_input)
    else:
        pubKey = RSA.generatePubKey((p-1)*(q-1))

    n = p*q

    conn.send(str(pubKey).encode())
    conn.send(str(n).encode())
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            cipher = data.decode()
            

print('Cipher:', cipher)
decryptedMessage = RSA.Decrypt(cipher,p,q,pubKey)
print('Decrypted Message: ',decryptedMessage)

# writing to file
with open("output.txt", "a") as a_file:
    a_file.write("Cipher: "+  cipher+ "\n")
    a_file.write("Decrypted Message: "+  str(decryptedMessage)+ "\n")
    a_file.close()
  