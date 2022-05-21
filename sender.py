import socket

from RSA import Encrypt

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65433  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    #s.sendall(b"Hello, world")
    
    j=0
    e=0
    n=0
    while j<2:
            data = s.recv(1024)
            if not data:
                break
            if j == 0:
                e = data.decode()
            if j == 1:
                n = data.decode()
            j+=1

    message = input("Enter the message to encrypt: ")
    s.sendall(str(Encrypt(message,n,e)).encode())

#print(f"Received {data!r}")
print("e: ", e)
print("n: ", n)
with open("e_n_file.txt", "a") as a_file:
    a_file.write(e + "\n")
    a_file.write(n)