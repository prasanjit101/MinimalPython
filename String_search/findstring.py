import os

text = input("Input string to be searched : ")
path = input("Input the path : ")


def getfiles(path):
    _file = 0
    os.chdir(path)
    files = os.listdir()
    for fileName in files:
        abs_path = os.path.abspath(fileName)
        if os.path.isdir(abs_path):
            getfiles(abs_path)
        if os.path.isfile(abs_path):
            _file = open(fileName, "r")
            if text in _file.read():
                _file = 1
                print(text + " found in ",end=" ")
                final_path = os.path.abspath(fileName)
                print(final_path)
                return True

    if _file == 0:
        print(text + " not found! ")
        return False


getfiles(path)
