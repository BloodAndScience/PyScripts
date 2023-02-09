import os
import shutil

# Source directory
sd = os.getcwd()

# Destination directory
dst_dir = "B:\\Git\\0IFC"

# File type (e.g. '.txt')
file_type = '.ifc'
ignore = '.git'

# Iterate through all files in the source directory
# Walk through all files and subdirectories in the source directory
for root, dirs, files in os.walk(sd):
    # Iterate through all files in the current directory
    for filename in files:
        if ignore in filename or not filename.endswith(file_type):
            continue
        # Construct the full source path
        src_path = os.path.join(root, filename)
        dst_path = os.path.join(dst_dir, filename)
        
        # Move the file to the destination directory

        if not os.path.isfile(dst_path):
            print(f'I copy to={dst_path}')
            shutil.copy(src_path, dst_path)
        else :
            print(f'File Already exist={dst_path}')

        
        

