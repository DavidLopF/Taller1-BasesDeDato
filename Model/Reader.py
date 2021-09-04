import os


class Reader:
    def __init__(self):
        pass


    def listDirectory():
            return os.listdir(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2')


    def knowBytes():
            if os.path.exists(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt'):

                x = str(os.path.getsize(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt'))
                return "EL ARCHIVO ESTA EN EL ESCRITORIO Y TIENE : " + x + " BYTES"
            else:
                x = str(os.path.getsize("../Resources/archivo-1.txt"))
                return "EL ARCHIVO ESTA EN EL DIRECTORIO RAIZ DEL PROGRAMA Y TIENE : " + x + " BYTES"

