from Model.Writer import createDirectory
from View.View import printConsole, captureInt, printMenu


class Contoller:
    def __init__(self):
        pass


printConsole("..::: BIENVENIDO :::...")

option = int(printMenu())
cont = 0

if option == 1:
    if cont == 0:
        printConsole("\n______________________________________________________________________")
        printConsole("CREANDO CARPETA ESPERE UN MOMENTO....")
        createDirectory("G_BD-2")
        printConsole("CARPETA CREADA CON EXITO :)")
        printConsole("______________________________________________________________________")
        printMenu()
        cont = + 1
    else:
        printConsole("YA SE HA CREADO EL DIRECTORIO EN EL ESCRITORIO...")
        printMenu()
