#Author: Pranav Sastry
#DateTime: 2021-03-30 10:49:40.477995 IST

import sys
import os
sys.path.append("/opt/anaconda3/lib/python3.7/site-packages/")
from PIL import Image

watermark_img = Image.open("watermark.png")

title = """\
            ___  ___           _
            |  \/  |          | |
 _ __  _   _| .  . | __ _ _ __| | __
| '_ \| | | | |\/| |/ _` | '__| |/ /
| |_) | |_| | |  | | (_| | |  |   <
| .__/ \__, \_|  |_/\__,_|_|  |_|\_|
| |     __/ |
|_|    |___/
                    - Pranav Sastry
"""
print(title)

def add_to_dir(dir_path):
    list_files = os.listdir(dir_path)
    for file in list_files:
        if(os.path.isfile("{}/{}".format(dir_path,file))):
            add_to_file("{}/{}".format(dir_path,file))

def add_to_file(file_path):
    try:
        source_img = Image.open(file_path)
        source_width,source_height = source_img.size
        watermark_width,watermark_height = watermark_img.size
        watermark_location_x = source_width - (watermark_width)
        watermark_location_y = source_height - (watermark_height)
        source_img.paste(watermark_img,(watermark_location_x,watermark_location_y),watermark_img)
        save_img(source_img,file_path)
    except:
        pass

def save_img(img_obj,file_path):
    img_obj.save(file_path)

try:
    operation = int(input("Directory/Individual file? [0/1] >> "))
except:
    print("Invalid input!")
    quit()

print()

if(operation==0):
    dir_path = input("Enter the path: ")
    if(os.path.exists(dir_path)):
        if(os.path.isdir(dir_path)):
            add_to_dir(dir_path)
            print()
            print("DONE!")
        else:
            print("File path specified. Specify the Directory path!")
    else:
        print("Invalid path!")
elif(operation==1):
    file_path = input("Enter the path: ")
    if(os.path.exists(file_path)):
        if(os.path.isfile(file_path)):
            add_to_file(file_path)
            print()
            print("DONE!")
        else:
            print("Directory path specified. Specify the File path!")
    else:
        print("Invalid path!")
else:
    print("Invalid input!")
