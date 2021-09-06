import mmap
import os


class Reader:
    def __init__(self):
        pass

    def listDirectory(self):
        return os.listdir(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2')

    def knowBytes(self):
        if os.path.exists(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt'):

            x = str(
                os.path.getsize(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt'))
            return "EL ARCHIVO ESTA EN EL ESCRITORIO Y TIENE : " + x + " BYTES"
        else:
            x = str(os.path.getsize("../Resources/archivo-1.txt"))
            return "EL ARCHIVO ESTA EN EL DIRECTORIO RAIZ DEL PROGRAMA Y TIENE : " + x + " BYTES"

    def knwoNumberLines(self):
        try:
            with open("../Resources/archivo-1.txt", encoding="utf8") as file:
                total = sum(1 for _ in file)
                return total
        except FileNotFoundError:
            with open(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt', encoding="utf8") as file:
                total = sum(1 for _ in file)
                return total