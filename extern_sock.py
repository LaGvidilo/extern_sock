import socket

def send_reponse(reponse="None",serv_address='127.0.0.1',send_port=21568,print_s=1):
	UDPSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = reponse+"\n" #ENVOI DE LA REQUETE
	addr = (serv_address, send_port)
	UDPSock.sendto(data,addr)
	if print_s==1:
		print (str(len(data.strip()))+"oct"," - To:",addr)

def recv_reponse(size_recv=1024,recv_port=21566,print_s=1):
	UDPSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listen_addr = ("",recv_port)
	UDPSock.bind(listen_addr)
	data,addr = UDPSock.recvfrom(size_recv)
	if print_s==1:
		print (data.strip()," - From:",addr)

def send_wait_recv_two(reponse_cmd="None",reponse="None",serv_address='127.0.0.1',send_port=21568,size_recv=1024,recv_port=21566,print_s=1):
	send_reponse(reponse_cmd,serv_address,send_port,print_s)	
	send_reponse(reponse,serv_address,send_port,print_s)
	recv_reponse(size_recv,recv_port,print_s)

def send_wait_recv(reponse="None",serv_address='127.0.0.1',send_port=21568,size_recv=1024,recv_port=21566,print_s=1):	
	send_reponse(reponse,serv_address,send_port,print_s)
	recv_reponse(size_recv,recv_port,print_s)
