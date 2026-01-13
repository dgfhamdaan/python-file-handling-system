from pathlib import Path
import os


"""IT give all file and folder existing in file handling folder"""
def readFileAndFolder():
    path = Path('') # current path to show
    items = list(path.rglob('*')) #list mean give value in your items
    for i, item in enumerate(items):
        print(f"{i+1} = {item}")

def createFile():

    try:
        readFileAndFolder()
        """create a file from user"""
        name = input("enter a file name:- ") # file name
        p = Path(name) # if name exist u get a path
        """it open and user write anything in your file """
        if not p.exists():
            with open(p,"w") as fs: 
             data = input("what do u want to write in file:- ")
             fs.write(data)
             print(f"YOUR FILE CREATED SUCCESSFULLY!")
        else:
          print("this file already exist!")
    except Exception as err:
        print(f"An error occur as {err}")


def readFile():
   
    try:
        readFileAndFolder()
        name = input("which file u want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

            print("READ FILE SUCESSFULLY!")    
        else:
            print("file doest not exist in folder")
    except Exception as err:
        print(f"An error occur as {err}")

def updateFile():
    try:
        readFileAndFolder()
        name = input("which file u want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("press 1 to change a name of your file")
            print("press 2 to overwrite he data of your file")
            print("press 3 to append some content in your file")

            res = int(input("tell your response:- ")) 

            if res == 1:
               name2 = input("tell your file name:- ")
               p2 = Path(name2)
               p.rename(p2)
        
            if res == 2:
                with open(p,"w") as fs:
                 data = input("tell what you want to write and this overwrite your data:- ")
                 fs.write(data)

            if res == 3:
                with open(p,"a") as fs:
                 data = input("tell what you want to append:- ")
                 fs.write(" "+data)  
          
    except Exception as err:
        print(f"An error occur as {err}")


def deleteFile():
    try: 
        readFileAndFolder()
        name = input("which file you want to delete:- ")
        p = Path(name)

        if p.exists() and p.is_file():

            os.remove(name)
            print("DELETE FILE SUCCESSFULLY!")

        else:
            print("file does not exist")
    except Exception as err:
        print(f"an error occurs as {err}")

print("press 1 to creating a file:- ")
print("press 2 to reading a file:- ")
print("press 3 to updating a file:- ")
print("press 4 to deletiona a file:- ")

check = int(input("enter a number:- "))

if check == 1:
    createFile()

if check == 2:
   readFile()

if check == 3:
    updateFile()

if check == 4:
    deleteFile()