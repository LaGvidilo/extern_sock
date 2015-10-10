from extern_sock import *


def send_msg(msg)
	send_wait_recv(msg,serv_address,send_port,size_recv,recv_port)


def __main__():
	msg=raw_input("reponse> ")
	serv_address=raw_input("serv_address> ")
	send_port=raw_input("send_port> ")
	size_recv=raw_input("size_recv> ")
	recv_port=raw_input("recv_port> ")
	send_msg(msg,serv_address,send_port,size_recv,recv_port)
	
__main__()