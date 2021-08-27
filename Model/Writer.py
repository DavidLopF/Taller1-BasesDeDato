import os


class Writer:
    def __init__(self):
        pass


def createDirectory(groupName: str):
    os.makedirs(os.path.join(os.environ["HOMEPATH"], "Desktop")+ "/" + groupName)
