import os
import shutil

def auto_folder(FOLDERNAME):

    pathdir = os.getcwd()

    for i in range (len(folderName)) :

        if os.path.exists(folderName[i]):
            
            while True:

                userInput = input(f"Are you sure tou want to replace {FOLDERNAME}?[Y/N]")

                if userInput == "Y":

                    shutil.rmtree(folderName[i])
                    path = os.path.join(pathdir, folderName[i])
                    os.mkdir(path)
                    print("1")
                    break

                elif userInput == "N":

                    print("0")
                    break

                else:

                    print("Invalid Option")
                    continue

        elif FOLDERNAME == "":

            print("0")

        else:
            path = os.path.join(pathdir, folderName[i])
            os.mkdir(path)
            print("1")
    
folderName = ["testfolder1","testfolder2"]
auto_folder(folderName)