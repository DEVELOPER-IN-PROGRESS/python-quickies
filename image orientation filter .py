import os
from PIL import Image
import shutil

folder_path = "D:\LOST.DIR\LANDSCAPE" # replace with your folder path
landscape  = f'{folder_path}\landscapes'
portrait = f'{folder_path}\portraits'

try:
    if not os.path.exists(landscape):
        os.mkdir(landscape)
    if not os.path.exists(portrait):
        os.mkdir(portrait)
except:
    pass

# loop through all files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    # check if file is an image
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        try:
            # open image and get properties
            with Image.open(file_path) as img:

                width = img.size[0]
                height = img.size[1]
                # print(f' {file_name} {width} {height}' )
                if width > height:
                    try:
                        shutil.move(os.path.join(folder_path,file_name), os.path.join(landscape , file_name))
                    except FileExistsError :
                        print('file exits')
                else:
                    try:
                        shutil.move(os.path.join(folder_path,file_name), os.path.join( portrait , file_name))
                    except FileExistsError:
                        print('file exits')
        except:
            pass
