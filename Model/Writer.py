import os
import shutil


class Writer:
    def __init__(self):
        pass

    def createDirectory(self, groupName):
        try:
            os.makedirs(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + groupName)
            return True
        except FileExistsError:
            return False

    def moveDirectory(self):
        try:
            shutil.move('../Resources/archivo-1.txt', os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2')
            return True
        except shutil.Error:
            return False

    def moveDirectoryMain(self):
        shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt',
                    '../Resources')

    def copyHalf(self):
        try:
            f = open("../Resources/archivo-1.txt", encoding="utf8")
            line = ""
            for i in range(240):
                if i >= 120:
                    line += f.readline(i)

            file = open("../Resources/nuevo-archivo_1.txt", "w")
            file.write(line)

            return "SE HA CREADO CON EXITO EN EL DIRECTORIO RESOURCES DEL PROGRAMA."

        except FileNotFoundError:
            f = open(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt',
                     encoding="utf8")
            line = ""
            for i in range(240):
                if i >= 120:
                    line += f.readline(i)

            file = open(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/nuevo-archivo_1.txt', "w")
            file.write(line)

            return "SE HA CREADO CON EXITO EN EL DIRECTORIO CON EL NOMBRE  DEL GRUPO EN EL ESCRITORIO."

    def createTxtAZ(self):
        alph = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

        try:
            f = open(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/nuevo-archivo_1.txt')
            line = []
            for i in range(240):
                if i >= 120:
                    line.append(f.readline(i))

            for i in range(len(alph)):
                file = open(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2/' + alph[i] + ".txt", "w")
                file.write(line[i])
            return "SE HA CREADO CORRECTAMENTE LOS 26 ARCHIVOS TXT, EN EL ESCRITORIO"

        except FileNotFoundError:
            f = open("../Resources/nuevo-archivo_1.txt")
            line = []
            for i in range(240):
                if i >= 120:
                    line.append(f.readline(i))

            for i in range(len(alph)):
                file = open("../Resources/" + alph[i] + ".txt", "w")
                file.write(line[i])

            return "SE HA CREADO CORRECTAMENTE LOS 26 ARCHIVOS TXT, EN EL DIRECTORIO RAIZ DEL PROGRAMA"