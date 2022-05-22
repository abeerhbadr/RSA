from email import message
import time
import RSA
import matplotlib.pyplot as plt

file1 = open('message.txt', 'r')
m_lines = file1.readlines()
message = ""
for m in m_lines:
    message = m
    
file2 = open('p_q_plot.txt', 'r')
lines = file2.readlines()

n_len_arr = []
time_arr = []

for i in range(len(lines)-1):
    p = int(lines[i])
    q = int(lines[i+1])
    
    n = p*q
    #n_len_arr.append(len(str(n)))
    n_len_arr.append(len(bin(n).replace("0b", "")))

    pubKey = RSA.generatePubKey((p-1)*(q-1))

    start_time = time.time()
    RSA.Encrypt(m,p*q,pubKey)
    end_time = time.time()

    time_taken = end_time - start_time
    time_arr.append(time_taken)


plt.plot(n_len_arr, time_arr)
plt.xlabel("Key Length")
plt.ylabel("Time")
plt.title("RSA Encryption Efficiency")
plt.show()
