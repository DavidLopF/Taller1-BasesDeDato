

class View:
    def __init__(self):
        pass


def printConsole(self: str):
    return print(self)


def captureDataStr(self: str):
    return input(self)


def captureInt(self: str):
    res = input(self)
    while not res.isnumeric():
       res = input(self)
    return res





def printMenu():
    print("SELECCION UNA OPCION\n" +
          "1. CREAR DIRECTORIO EN EL ESCRITORIO.\n" +
          "2. CAMBIAR UBICACION DEL ARCHIVO DESCARGADO AL DIRECTORIO CREADO.\n" +
          "3. LISTAR CONTENIDO DEL DIRECTORIO DE LA CARPETA CON EL NOMBRE DEL CODIGO DEL GRUPO.\n" +
          "4. MUESTRE EL TAMAÑO DE BYTES DEL ARCHIVO.\n" +
          "5. COPIE LA ULTIMA MITAD DE LOS REGISTROS/LINEAS DEL ARCHIVO A OTROO ARCHIVO LLAMADO nuevo-archivo_1.txt.\n" +
          "6. GENERAR 26 ARCHIVOS DEL LA A A LA Z.\n" +
          "________________________________________________________________________________________________________________")
    return captureInt("SELECIONE UNA OPCION: ")

