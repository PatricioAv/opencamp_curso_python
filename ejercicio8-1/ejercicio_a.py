def escribir_archivo(ruta_a_archivo, datos):
    """
    Crea y escribe el contenido del segundo argumento 'datos'
    en la ruta pasada como primer argumento
    """
    with open(ruta_a_archivo, 'w') as file:
        file.write(datos)


def leer_archivo(ruta_a_archivo):
    """
    Lee y retorna el contenido del archivo pasado como argumento
    """
    with open(ruta_a_archivo, 'r') as file:
        datos_archivo = file.read()
        return datos_archivo


def main():
    archivo = './archivo.txt'
    datos = "Escribiendo en archivo de prueba 'archivo.txt'\n"
    datos += "utilizando un administrador de contexto.\n"
    datos += "'with open(file, modo) as alias:'\n"
    datos += "para cerrar el archivo automáticamente despues de su uso."

    escribir_archivo(archivo, datos)

    dato_archivo = leer_archivo(archivo)
    print(dato_archivo)
    

if __name__ == '__main__':
    main()
