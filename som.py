import os

# Get the directory of the script
script_directory = os.path.dirname(__file__)

# Specify the folder path relative to the script directory
folder_path = os.path.join(script_directory, 't')

# Iterate through items (files and subfolders) in the folder
for item in os.listdir(folder_path):
    item_path = os.path.join(folder_path, item)
    if os.path.isfile(item_path):
        print(f'File: {item}')
    elif os.path.isdir(item_path):
        print(f'Subfolder: {item}')