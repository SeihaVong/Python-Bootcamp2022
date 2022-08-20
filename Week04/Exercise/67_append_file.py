import datetime


def append_file(filename):

    curTime = datetime.datetime.now()
    currenTimeFor = curTime.strftime("[%d/%m/%Y %X]")

    while True:
        userInput = input(f"$:")
        if userInput == "EXIT":
            break
        
        else:
            f = open(filename, "a")
            f.write(f"\n{currenTimeFor}{userInput}")
            f.close()
            continue



append_file("Hello World3.txt")