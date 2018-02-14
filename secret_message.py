#get all the file name # for each for file rename the file
import os
def rename_file():
    #list all the files in the directory
    file_list=os.listdir(r"/Users/nourannouh/Desktop/prank")
    #print file_list
    
    #get current working directory
    saved_path=os.getcwd() 
    print ("current Working Directory is "+saved_path)
    
    #change directory
    os.chdir(r"/Users/nourannouh/Desktop/prank")
    
    #for each file name in the file list
    #rename the old file by the new file name 
    for file_name in file_list:
        print ("old Name"+file_name)
        print ("new name"+file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,"0123456789"))
    
    os.chdir(saved_path)#change directory back 
rename_file()