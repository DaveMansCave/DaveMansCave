import os
import shutil
import re
list_files = os.listdir()
file = []
current_path = '/home/dahu'
desired_path = '/home/dahu/pcaps'
for i in list_files:
    quoted_files = f"{i}"
    file.append(quoted_files)
for i in file:
    if i.endswith('.pcapng'):
        source_path = current_path + '/' + i
        shutil.move(source_path, desired_path)
        
        
        
        
