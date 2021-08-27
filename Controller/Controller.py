from Model.Writer import createDirectory, moveDirectory , moveDirectoryMain
from View.View import printConsole, captureInt, printMenu


class Contoller:
    def __init__(self):
        pass


printConsole("..::: BIENVENIDO :::...")


def selecOptionMenu():
    option = int(printMenu())
    if option == 1:

         if createDirectory("G_BD-2"):
             printConsole("\n______________________________________________________________________\n")
             printConsole("CREANDO CARPETA ESPERE UN MOMENTO....")
             printConsole("CARPETA CREADA CON EXITO :)\n")
             printConsole("______________________________________________________________________")
         else:
                printConsole("\n______________________________________________________________________\n")
                printConsole("LA CARPETA YA HA SIDO CREADA....\n\n")
                printConsole("\n______________________________________________________________________")
                selecOptionMenu()


    elif option == 2:
        if moveDirectory():
            printConsole("\n______________________________________________________________________\n")
            printConsole("MOVIENDO TXT A CARPETA DEL ESCRITORIO....")
            printConsole("\n______________________________________________________________________\n")
            selecOptionMenu()
        else:
            printConsole("LA CARPETA YA SE ECUENTRA EN EL ESCRITORIO\n" +
                         '¿ DESEA DEJARLA AHI O MOVERLA AL DIRECTORIO RAIZ DEL PROGRAMA ?' +
                         '\n  1. Si' +
                         '\n  2. NO')
            aux = int(captureInt('\nSELECCIONE UNA OPCION: '))

            if aux == 1:
                moveDirectoryMain()
                printConsole("\n______________________________________________________________________\n")
                printConsole("MOVIENDO TXT A CARPETA RAIZ DEL PROGRAMA....")
                printConsole("\n______________________________________________________________________\n")
                selecOptionMenu()
            else:
               selecOptionMenu()

selecOptionMenu()