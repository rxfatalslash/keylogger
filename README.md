Al ejecutar el script se graban las teclas pulsadas en un archivo llamado keys que se encuentra en una carpeta oculta

# Uso
En el remitente escribimos el correo desde el que queremos que se envíen los correos
<br>
<img src="assets/ejemplos_email.png" alt="Ejemplos email" width="400px">
<br><br>
Accede a los ajustes de tu cuenta de Gmail y asegurate de que la verificación en dos pasos está activada
<img src="assets/seguridad.png" alt="Seguridad" width="400px">
<br>
<img src="assets/doble_factor.png" alt="Doble factor" width="600px">
<br><br>
Para poder usar la contraseña, accede a <a href="https://myacount.google.com/apppasswords">Contraseñas de aplicaciones</a>
<br>
<img src="assets/app_passwords.png" alt="Contraseñas de aplicaciones" width="400px">
<br><br>
Copia la clave generada en el valor de la variable password del script de envío
<br>
Cambia el valor de **_"RUTA"_** en ambos scripts por la ruta que quieras, es recomendable usar la ruta **_"C:/Users/{user}/.../keys"_** donde **_{user}_** es el usuario del sistema, para evitar errores en la creación de la carpeta oculta por la falta de permisos
<br>
<img src="assets/ejemplos_ruta.png" alt="Ejemplos ruta" width="400px">
## Script de envío
Cada 60 segundos se enviará el contenido del archivo keys en texto plano al correo que hayas elegido
<br>
Puedes cambiar la frecuencia de envío en **_"time.sleep(INTERVALO_EN_SEGUNDOS)"_**
## Ejecución
Ejecuta los script con los comandos en terminales distintas
```
python keylogger.py
python send.py
```
En futuras versiones se corregirá para que las funciones se ejecuten desde el mismo script
