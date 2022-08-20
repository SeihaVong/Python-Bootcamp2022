import os.path


def write_file(FILENAME, content):

    if os.path.exists(FILENAME):

        while True:
            userInput = input(f"Are you sure you want to replace {FILENAME}?[Y/N]")

            if userInput == "Y":
                f = open(FILENAME, "w")
                f.write(content)
                print("1")
                break

            elif userInput == "N":
                print("0")
                break

            else:
                print("Invalid Option")
                continue

    else:
        f = open(FILENAME, "w")
        f.write(content)
        print("1")


write_file("Hello World2.txt","Hello World")