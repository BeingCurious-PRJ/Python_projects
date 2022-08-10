import os,re, os.path

mypath = r'give the path of the folder whose files needs to be deleted'
for root, dirs, files in os.walk(mypath): # loops through the folder
    for file in files:
        os.remove(os.path.join(root,file)) #deletes each file present in the folder