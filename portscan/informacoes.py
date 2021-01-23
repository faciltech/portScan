#!/usr/bin/python
print("    _________   ____________  ____________________  __");
print("   / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /");
print("  / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ / ");
print(" / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /  ");
print("/_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/   ");
print("              ");
print("Autor: Eduardo Amaral - eduardo4maral@protonmail.com")
def escolher_listaPortas():
	portas_top10 = [21,22,23,25,80,110,139,443,445,3389]
	portas_top20 = [21,22,23,25,80,110,139,443,445,3389,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
	portas_top50 = [21,22,23,25,80,110,139,443,445,3389,135,139,143,443,445,993,995,1723,3306,3389,5900,8080,3389,5060,5666,5900,6001,8000,8080,8443,8888,10000,32768,49152,49154]
	portas_total = range(1,65535)
	print("Selecione uma lista de Portas: ")
	print("0 - Uma porta especifica")
	print("1 - Lista top 10")
	print("2 - Lista top 20")
	print("3 - Lista top 50")
	print("4 - Verificar as 65535 portas -- OBS: Levará muito tempo !!!")
	escolha = input("\n>>> ")
	lista_escolhida = []

	if (escolha == '0' ):
		port = input("Digite a porta: ")
		portas_zero = [int(port)] 
		lista_escolhida = portas_zero
		return lista_escolhida
	elif (escolha == '1' ):
		lista_escolhida = portas_top10
		return lista_escolhida
	elif (escolha == '2' ):
		lista_escolhida = portas_top20
		return lista_escolhida
	elif (escolha == '3' ):
                lista_escolhida = portas_top50
                return lista_escolhida
	else:
		lista_escolhida = portas_total
		return lista_escolhida

def mostraLinha():
	print("------------------------------------------------------")
