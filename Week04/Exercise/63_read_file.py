from pathlib import Path

def read_file(string):

    pa = Path(string)

    if pa.is_file():
        
        f = open(string, "r")
        readTextInList = f.readlines()
        readTextInString = "".join(readTextInList)        
        print(f"{readTextInString}")
        
        
    else:
        print(f"Invalid FILENAME")

read_file()