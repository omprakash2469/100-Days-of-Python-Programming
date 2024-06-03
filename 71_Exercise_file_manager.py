# Filter files according to file types

import os, shutil

src = "C:/Users/admin/Pictures/wallpaper/Home - Blingg Jewelry_files/"
dest = "C:/Users/admin/Downloads/Jwellery/"

files = os.listdir(src)

for file in files:
    file_type = file.split(".")[-1]

    # Check if the folder exists
    folder_path = os.path.join(dest, file_type)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    print(f"{file} moved successfully!")
    # Move to their specific directories
    shutil.copy(src + file, folder_path + "/" + file)