extern_sock_udp - PERMET UNE UTILISATION SIMPLE DE UDP
========================================================



Vous pouvez l'installer sur ubuntu:
	sudo python setup.py install

Exemple d'usage pour crée un serveur(R sera la donnée de retour):
	>>>import extern_sock_udp as udp
	>>>R = udp.recv_wait_send(reponse="Done",print_s=0)

Exemple d'usage pour crée un client:
	>>>import extern_sock_udp as udp
	>>>R = udp.send_wait_recv(serv_address=serv_address,reponse=msg,send_port=21566,recv_port=21568,print_s=0)

Ce code est sous licence GPL-2.
