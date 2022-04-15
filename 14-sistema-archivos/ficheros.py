from io import open
import pathlib

ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta,"a+")

archivo.write("Soy un texto escrito desde python...\n")
archivo.close()