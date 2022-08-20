import os

def current_folder():
    

    lstFolderfile = []
    
    currentDir = os.listdir() 

    for i in range (len(currentDir)):
        
        if os.path.isdir(currentDir[i]):
            lstFolderfile.append((currentDir[i],"Folder"))
            
        else:
            os.path.isfile(currentDir[i])
            lstFolderfile.append((currentDir[i],"File"))
            

    print(lstFolderfile)

current_folder()