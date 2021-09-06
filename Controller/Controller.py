from Model.Reader import *
from Model.Writer import *
from View.View import *


class Controller:
    def __init__(self):
        printConsole("..::: BIENVENIDO :::...")
        self.reader = Reader()
        self.writer = Writer()
        self.selectOptionMenu()

    def selectOptionMenu(self):
        option = int(printMenu())
        if option == 1:

            if self.writer.createDirectory("G_BD-2"):
                printConsole("\n______________________________________________________________________\n")
                printConsole("CREANDO CARPETA ESPERE UN MOMENTO....")
                printConsole("CARPETA CREADA CON EXITO :)\n")
                printConsole("______________________________________________________________________")
            else:
                printConsole("\n______________________________________________________________________\n")
                printConsole("LA CARPETA YA HA SIDO CREADA....\n\n")
                printConsole("\n______________________________________________________________________")
                self.selectOptionMenu()

        elif option == 2:
            if self.writer.moveDirectory():
                printConsole("\n______________________________________________________________________\n")
                printConsole("MOVIENDO TXT A CARPETA DEL ESCRITORIO....")
                printConsole("\n______________________________________________________________________\n")
                self.selectOptionMenu()
            else:
                printConsole("LA CARPETA YA SE ECUENTRA EN EL ESCRITORIO\n" +
                             '¿ DESEA DEJARLA AHI O MOVERLA AL DIRECTORIO RAIZ DEL PROGRAMA ?' +
                             '\n  1. Si' +
                             '\n  2. NO')
                aux = int(captureInt('\nSELECCIONE UNA OPCION: '))

                if aux == 1:
                    self.writer.moveDirectoryMain()
                    printConsole("\n______________________________________________________________________\n")
                    printConsole("MOVIENDO TXT A CARPETA RAIZ DEL PROGRAMA....")
                    printConsole("\n______________________________________________________________________\n")
                    self.selectOptionMenu()
                else:
                    self.selectOptionMenu()

        elif option == 3:
            printConsole("\n______________________________________________________________________\n")
            printConsole("LISTA DEL DIRECTORIO G_BD-2 :\n" + str(self.reader.listDirectory()))
            printConsole("\n______________________________________________________________________\n")
            self.selectOptionMenu()
        elif option == 4:
            printConsole("\n______________________________________________________________________\n")
            printConsole(self.reader.knowBytes() + '\n')
            printConsole("\n______________________________________________________________________\n")
            self.selectOptionMenu()

        elif option == 5:
            printConsole("\n______________________________________________________________________\n")
            printConsole("EL ARCHIVO TIENE: " + str(self.reader.knwoNumberLines()) + ' LINEAS\n')
            printConsole("\n______________________________________________________________________\n")
            self.selectOptionMenu()
        elif option == 6:
            printConsole("\n______________________________________________________________________\n")
            printConsole(self.writer.copyHalf() + '\n')
            printConsole("ARCHIVOS COPIADOS CORRECTAMENTE :)")
            printConsole("\n______________________________________________________________________\n")
            self.selectOptionMenu()
        elif option == 7:
            printConsole("\n______________________________________________________________________\n")
            printConsole(self.writer.createTxtAZ() + '\n')
            printConsole("\n______________________________________________________________________\n")
            self.selectOptionMenu()
