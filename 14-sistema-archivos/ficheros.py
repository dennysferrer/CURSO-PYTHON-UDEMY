from io import open
import pathlib
import shutil

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

archivo.write("Soy un texto escrito desde python...\n")
archivo.close()

# Copiar archivo

"""
ruta2 = str(pathlib.Path().absolute()) + "/fichero_texto_copiado.txt"
shutil.copyfile(ruta, ruta2)
"""

# Mover un archivo
"""
ruta_destino = str(pathlib.Path().absolute()) + "/archivos_copiados/fichero_copiado.txt"
shutil.move(ruta, ruta_destino)
"""

# Eliminar archivos
import os
ruta_destino = str(pathlib.Path().absolute()) + "/archivos_copiados/fichero_copiado.txt"
os.remove(ruta_destino)

# Comprobar si el archivo existe

import os.path

if os.path.isfile(ruta):
    print("El archivo existe")
else:
    print("El archivo no existe")




