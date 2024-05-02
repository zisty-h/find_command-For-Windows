import os
import sys
from time import sleep
from datetime import datetime as time
# get folders - get files for loop

def getFolders(root):
    objlist = os.listdir(root)
    folders = []
    for obj in objlist:
        path = os.path.join(root, obj)
        if os.path.isdir(path):
            folders.append(path)

    return folders
def main():
    Text = sys.argv[1]
    files = []
    folders = []
    root = os.getcwd()
    result = getFolders(root)
    if len(result) > 0:
        for folder in result:
            print(folder)
            folders.append(folder)
    isFolder = True

    while isFolder:
        for folder in folders:
            result = getFolders(os.path.join(root, folder))
            if len(result) > 0:
                for folder in result:
                    print(folder)
                    folders.append(folder)
            else:
                isFolder = False


    for folder in folders:
        print("Searching : " + folder)
        folder_result = os.listdir(folder)
        for file in folder_result:
            print(f"[INFO {time.now()}] ANALYSIS FILE: {file}")
            if Text in file:
                files.append(os.path.join(root, folder, file))
                sleep(0.1)

    os.system("cls")
    if len(files) == 0:
        print("Found include " + str(len(files)) + " files")
        return
    print("### FINISHED ANALYSIS FILE ###")
    for file in files:
        print(file)
    return files

if __name__ == "__main__":
    main()