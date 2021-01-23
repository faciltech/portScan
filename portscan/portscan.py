#!/usr/bin/python3
import socket
from datetime import datetime
import informacoes

def mensagem(msg):
	print("-" * 30)
	print(msg)
	print("-" * 30)

def novamente():
	res = input("deseja fazer nova consulta? (Sim [1]/Não[0]): ")
	if (res == '1'):
		port_scan()
		print("")
		novamente()
	else:
		mensagem('      Fim do codigo   ')
		exit()

ip = input("Digite seu ip: ")
mensagem('	Inicio do Programa	')
def port_scan():
#	ip = input("Digite seu ip: ")
	lista_portas = informacoes.escolher_listaPortas()
	print("Iniciando os scans no Ip: ",ip)
	for porta in lista_portas:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(0.5)
		if (s.connect_ex((ip,porta)) == 0):
			print("A porta [ABERTA]",porta)
			s.close()
port_scan()
print("")
novamente()
