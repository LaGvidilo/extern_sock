#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
	CE CODE PERMET DE CREE FACILEMENT UN SERVEUR OU UN CLIENT UDP
 
	Exemple d'usage pour crée un serveur(R sera la donnée de retour):
		>>>import extern_sock_udp as udp
		>>>R = udp.recv_wait_send(reponse="Done",print_s=0)

	Exemple d'usage pour crée un client:
		>>>import extern_sock_udp as udp
		>>>R = udp.send_wait_recv(serv_address=serv_address,reponse=msg,send_port=21566,recv_port=21568,print_s=0)

"""
import socket
__version__ = "0.0.3"
# ENVOI
def send_reponse(reponse="None",serv_address='127.0.0.1',send_port=21568,print_s=1):
	UDPSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	data = reponse+"\n"
	addr = (serv_address, send_port)
	UDPSock.sendto(data,addr)
	if print_s==1:
		print (str(len(data.strip()))+"oct"," - To:",addr)

# RECEPTION
def recv_reponse(size_recv=1024,recv_port=21566,print_s=1):
	UDPSock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listen_addr = ("",recv_port)
	UDPSock.bind(listen_addr)
	data,addr = UDPSock.recvfrom(size_recv)
	if print_s==1:
		print (data.strip()," - From:",addr)
	return data.strip()

# ENVOI DOUBLE, ATTENTE ACCUSE DE RECEPTION
def send_wait_recv_two(reponse_cmd="None",reponse="None",serv_address='127.0.0.1',send_port=21568,size_recv=1024,recv_port=21566,print_s=1):
	send_reponse(reponse_cmd,serv_address,send_port,print_s)	
	send_reponse(reponse,serv_address,send_port,print_s)
	R=recv_reponse(size_recv,recv_port,print_s)
	return R

# ENVOI, ATTENTE ACCUSE DE RECEPTION
def send_wait_recv(reponse="None",serv_address='127.0.0.1',send_port=21568,size_recv=1024,recv_port=21566,print_s=1):	
	send_reponse(reponse,serv_address,send_port,print_s)
	R=recv_reponse(size_recv,recv_port,print_s)
	return R

# RECEPTION + ENVOI ACCUSE DE RECEPTION
def recv_wait_send(reponse="None",serv_address='127.0.0.1',send_port=21568,size_recv=1024,recv_port=21566,print_s=1):	
	R=recv_reponse(size_recv,recv_port,print_s)
	send_reponse(reponse,serv_address,send_port,print_s)
	return R
	
