"""Implemente un programa que solicite al usuario el nombre de un archivo y luego genere el tipo de
archivo MIME correspondiente. Si el nombre del archivo termina en cualquiera de estos sufijos (sin
importar el uso de mayúsculas y minúsculas) :
- .gif
- .jpg
- .jpeg
- .png
- .pdf
- .txt
- .zip
Si el nombre del archivo termina con algún otro sufijo que no se encuentra en la lista o no tiene
ningún sufijo, en su lugar su programa deberá devolver application/octet-stream.
Ejemplos:
Nombre Archivo: happy.jpg Salida Esperada: image/jpeg
Nombre Archivo: document.pdf Salida Esperada: application/pdf
Para conocer los tipos MIME a utilizar, puede revisar el siguiente enlace.
Nota:
- El empleo de diccionarios podría ayudar con esta tarea.
- El uso de métodos de cadena sería muy útil al momento de separar el nombre del archivo de
su extensión"""

nombre_archivo = input("Ingrese el nombre del archivo: ")

# Obtener la extensión del archivo
punto_index = nombre_archivo.rfind('.')
if punto_index != -1:
    extension = nombre_archivo[punto_index + 1:].lower()
else:
    extension = ""

# Crear un diccionario con las correspondencias de extensiones a tipos MIME
tipos_mime = {
    'gif': 'image/gif',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'png': 'image/png',
    'pdf': 'application/pdf',
    'txt': 'text/plain',
    'zip': 'application/zip',
}

# Obtener el tipo MIME correspondiente o 'application/octet-stream' si no se encuentra
tipo_mime = tipos_mime.get(extension, 'application/octet-stream')

print("Salida Esperada:", tipo_mime)
