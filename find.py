import os
import sys
from time import sleep

def find(file_list, text):
    isFolder = True
    while isFolder:
        Text = text.replace("*", "")
        find_list = []
        search_folders = []
        for filename in file_list:
            if os.path.isfile(filename):
                if Text in filename:
                    abs_filename = os.path.abspath(filename)
                    find_list.append(abs_filename)
            else:
                search_folders.append(filename)

        print("Folders: " + str(search_folders))
        for folder in search_folders:
            folder_path = os.path.join(os.getcwd(), folder)
            print("Folder: " + folder_path)
            files = os.listdir(folder_path)
            for file in files:
                print("File: " + file)
                if Text in file:
                    abs_file_path = os.path.join(folder_path, file)
                    find_list.append(abs_file_path)
    sleep(10)
    return find_list

def main():
    file_list = os.listdir('.')
    in_file = find(file_list, sys.argv[1])
    os.system("cls")
    for file in in_file:
        print(file)
    return

if __name__ == '__main__':
    main()