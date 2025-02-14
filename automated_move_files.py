import os
import shutil
import sys
#this function will take two arguments, the path of the file
#and the path of the directory you want to go to
def move_files():
    if len(sys.argv) != 3:
           print("Usage 'script' </path/to/file> </path/to/dir>")
    source_path = sys.argv[1]
    dest_path = sys.argv[2]
    if os.path.isfile(source_path) == False:
        print("Check your file path")
    if os.path.isdir(dest_path) == False:
        os.mkdir(dest_path)
        print("Directory created at" + " " + dest_path)
    shutil.move(source_path, dest_path)
    print("File moved successfully")
    

        
        
        
        
