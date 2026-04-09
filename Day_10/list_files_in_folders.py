import os

folder_paths=input("please enter the list of folder names separated by space : ").split()

for folder in folder_paths:
    try:
        files=os.listdir(folder)
    except FileNotFoundError:
        print("the folder does not exist "+ folder)
        continue
    except PermissionError:
        print("you do not have permission to open the folder: "+ folder)
        continue
    print("files in the folder "+ folder)
    for file in files:
        print(file)