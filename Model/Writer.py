import os
import pathlib
import shutil


class Writer:
    def __init__(self):
        pass


def createDirectory(groupName: str):
    try:
        os.makedirs(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + groupName)
        return True
    except FileExistsError:
        return False


def moveDirectory():
    try:
        shutil.move('../Resources/archivo-1.txt', os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2')
        return True
    except shutil.Error:
        return False


def moveDirectoryMain():
    shutil.move(os.path.join(os.environ["HOMEPATH"], "Desktop") + "/" + 'G_BD-2' + '/archivo-1.txt',
                '../Resources')
