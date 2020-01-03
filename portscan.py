#!/usr/bin/python
import socket,sys
print "    _________   ____________  ____________________  __"
print "   / ____/   | / ____/  _/ / /_  __/ ____/ ____/ / / /"
print "  / /_  / /| |/ /    / // /   / / / __/ / /   / /_/ / "
print " / __/ / ___ / /____/ // /___/ / / /___/ /___/ __  /  "
print "/_/   /_/  |_\____/___/_____/_/ /_____/\____/_/ /_/   "
print "                                                      "
print "#Autor: Eduardo Amaral ";
print "#youtube.com/faciltech";
if len(sys.argv) <2:
	print "Use da seguinte forma: ./portscan 127.0.0.1"
	print "Use da seguinte forma: ./portscan dominio.com.br 80"
else:
	if len(sys.argv) == 3:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                if s.connect_ex((sys.argv[1], int(sys.argv[2]))) == 0:
                        print "Porta",sys.argv[2]," [ABERTA]"
                        s.close()
                else:
                        print "Porta",sys.argv[2]," [FECHADA]"
                        s.close()	
	else:
		print "Analisando portas ..."
                for port in range(1,65535):
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        if s.connect_ex((sys.argv[1], port)) == 0:
                                print "Porta ",port," [ABERTA]"
                                s.close()
