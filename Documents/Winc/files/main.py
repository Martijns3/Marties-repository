__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

# ----------------------------------------------------------------------------------------------------------------------------


def clean_cache():

    dir_path = os.path.join(os.getcwd(), "files/cache")
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)


# ----------------------------------------------------------------------------------------------------------------------------

from zipfile import ZipFile


def cache_zip(zip_file_path: str, cache_dir_path: str):
    with ZipFile(zip_file_path) as zipObj:
        zipObj.extractall(cache_dir_path)

    os.listdir(os.path.join(os.getcwd(), "files/cache"))


# ----------------------------------------------------------------------------------------------------------------------------


def cached_files():
    dir_contents = os.listdir(os.path.join(os.getcwd(), "files/cache"))
    file_list = []
    for entry in dir_contents:
        fullPath = os.path.join(os.getcwd(), "files/cache", entry)
        if os.path.isdir(fullPath):
            pass
        else:
            file_list.append(fullPath)

    return file_list


# ----------------------------------------------------------------------------------------------------------------------------


def find_password(file_list):

    for x in file_list:
        openfile = open(x, "r")
        line = openfile.readline()
        while line != "":
            line = openfile.readline()
            if "password" in line:
                passkey = str(line.replace("password: ", "").rstrip("\n"))
                return passkey


# ----------------------------------------------------------------------------------------------------------------------------


def main():
    clean_cache()
    cache_zip(
        (os.path.join(os.getcwd(), "files/data.zip")),
        (os.path.join(os.getcwd(), "files/cache")),
    )
    cached_files()
    find_password(cached_files())


# ----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
