import os
import shutil


def organize_downloads(folder="C:\Users\smsma\Downloads"):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)
        if os.path.isfile(path):
            ext = file.split(".")[-1].lower()
            new_dir = os.path.join(folder, ext)
            os.makedirs(new_dir, exist_ok=True)
            shutil.move(path, os.path.join(new_dir, file))
organize_downloads()
