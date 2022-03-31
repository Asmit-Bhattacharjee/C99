import os
import shutil

path = input("Enter the name of the directory to be organised: ")

#This will create a variable which will list all the files
list_of_files = os.listdir(path)

#This will go through each and every file
for file in list_of_files:
    name,ext = os.path.splitext(file)

    #This is going to store the extension type 
    ext = ext[1:]

    #This forces the next iteration if its a directory
    if ext=='':
        continue

    #This will move the file to the directory if the ext directory is already there
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)