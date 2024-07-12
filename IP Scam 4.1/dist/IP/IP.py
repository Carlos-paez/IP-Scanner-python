import os
import sys
import platform
from datetime import datetime

ip = input("Ingresa la IP: ")
ipDividida = ip.split('.')
try:
    red = ipDividida[0] + '.' + ipDividida[1] + '.' + ipDividida[2] + '.'
    comienzo = int(input("Ingresa el número de comienzo de la subred: "))
    fin = int(input("Ingresa el número en el que deseas acabar el barrido: "))
except:
    print("[!] Error")
    sys.exit(1)

if platform.system() == "Windows":
    ping = "ping -n 1"
else:
    ping = "ping -c 1"

tiempoInicio = datetime.now()
print(f"[*] El escaneo se está realizando desde {red}{comienzo} hasta {red}{fin}")

ip_count = 0
ip_activas = []

for subred in range(comienzo, fin + 1):
    direccion = red + str(subred)
    response = os.popen(ping + " " + direccion)
    for line in response.readlines():
        if "ttl" in line.lower():
            print(f"{ip_count + 1}. {direccion} está activo")
            ip_activas.append(direccion)
            ip_count += 1
            break

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print(f"[*] El escaneo ha durado {tiempo}\n")
print(f"[*] Se encontraron {ip_count} direcciones IP activas\n")

if ip_activas:
    ver_inactivas = input("¿Deseas ver las direcciones IP inactivas? (Sí/No): ")
    if ver_inactivas.lower() == "sí":
        for subred in range(comienzo, fin + 1):
            direccion = red + str(subred)
            if direccion not in ip_activas:
                print(f"{direccion} está inactivo")
else:
    print("No se encontraron direcciones IP activas.")
finalizar=str(input("le a sido util este sistema de escaneo de direcciones IP"))