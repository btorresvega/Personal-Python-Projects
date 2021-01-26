#This is a script to move files with a certain extension type from a source directory to a destination path
# Simply replace the *source , * destination and *extension type 


import shutil
import os
import sys
import time #I added this to use file system watcher in the future
from watchdog.observers import Observer #I added this to use file system watcher in the future
from watchdog.events import FileSystemEventHandler #I added this to use file system watcher in the future
from pathlib import Path

source = r"C:\Users\garci\Downloads"
destination = r"C:\Users\garci\Desktop\Scaleit - Voice Messages"

files = os.listdir(source)

destination_files = os.listdir(destination)

for file in files:
 name, extension = os.path.splitext(file)
 if extension == '.wav':
    fileBaseName = os.path.basename(file)
    destination = os.path.join(destination,fileBaseName)
    new_path = shutil.move(f"{source}/{file}", destination)
    print(new_path)
    
       
            
          
 
              

               
           
