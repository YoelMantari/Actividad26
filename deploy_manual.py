import sys

respuesta = input("confirmas deploy? (s/n): ")
if respuesta.lower() != 's':
    print("deploy cancelado")
    sys.exit(1)
else:
    print("deploy manual ejecutado")
