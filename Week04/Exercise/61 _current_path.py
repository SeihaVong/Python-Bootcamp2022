import os

def current_path():
    path = os.getcwd()
    pathL = []
    pathL.append(path)
    pathString = "".join(pathL)

    print(pathString)

current_path()