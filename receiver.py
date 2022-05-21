import socket
import RSA

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65433  # Port to listen on (non-privileged ports are > 1023)  #changed it from 65432 to 65433 bec it gave an error

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    # Using readlines()
    file1 = open('P_Q_File.txt', 'r')
    Lines = file1.readlines()
  
    #count = 0
    # Strips the newline character
    pandq = []
    for line in Lines:
        #count += 1
        #print("Line{}: {}".format(count, line.strip()))
        pandq.append(int(line.strip()))

    p = pandq[0]
    q = pandq[1]
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
            #conn.sendall(data)
        decryptedMessage = RSA.Decrypt(cipher,p,q,pubKey)
        print('Decrypted Message: ',decryptedMessage)
        # writing to file
        with open("OutputFile.txt", "a") as a_file:
            a_file.write("\n")
            a_file.write(decryptedMessage)
  