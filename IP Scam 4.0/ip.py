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

ip_activas = []
ip_inactivas = []

for subred in range(comienzo, fin + 1):
    direccion = red + str(subred)
    response = os.popen(ping + " " + direccion)
    for line in response.readlines():
        if "ttl" in line.lower():
            ip_activas.append(direccion)
            break
    else:
        ip_inactivas.append(direccion)

tiempoFinal = datetime.now()
tiempo = tiempoFinal - tiempoInicio
print(f"[*] El escaneo ha durado {tiempo}\n")

opcion = input("¿Quieres ver las IP activas (A) o las inactivas (I)?: ").lower()

if opcion == 'a':
    print(f"[*] Se encontraron {len(ip_activas)} direcciones IP activas:")
    for i, ip_activa in enumerate(ip_activas, start=1):
        print(f"{i}. {ip_activa}")
elif opcion == 'i':
    print(f"[*] Se encontraron {len(ip_inactivas)} direcciones IP inactivas:")
    for i, ip_inactiva in enumerate(ip_inactivas, start=1):
        print(f"{i}. {ip_inactiva}")
else:
    print("Opción no válida. Debes elegir 'A' o 'I'.")

fin=str(input("¿Le ha sido util este programa?"))

