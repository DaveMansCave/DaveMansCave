import os
import shutil
files = []
path = '/home/damasta'
dest_path = '/home/damasta/txt'
list_files = os.listdir()
for i in list_files:
    files.append(f"{i}")
for i in files:
    if i.endswith('.txt'):
        source_path = path + '/' + i
        shutil.move(source_path, dest_path)
