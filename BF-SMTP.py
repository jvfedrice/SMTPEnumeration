#!/usr/bin/python
import socket,sys

file  = open("lista.txt")
for linha in file:
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	tcp.connect((sys.argv[1],25))
	banner = tcp.recv(1024)
	tcp.send("VRFY "+linha)
	user = tcp.recv(1024)
	print user
  
  
  #To make the code cleaner, we can put it to bring only the users that exist on the host. 
  #In the response that the script brings to all users on the host, it brings us the code 252. 
  #Therefore, we can add after the "print user":
  if re.search("252",user):
	  print "Usuário encontrado:  "+user
