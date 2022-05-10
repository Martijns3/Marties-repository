__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

# ----------------------------------------------------------------------------------------------------------------------------


def clean_cache():

    dir_path = "/Users/Martijn/Documents/Winc/files/cache"
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)


# ----------------------------------------------------------------------------------------------------------------------------

from zipfile import ZipFile


def cache_zip(zip_file_path: str, cache_dir_path: str):
    with ZipFile(zip_file_path) as zipObj:
        zipObj.extractall(cache_dir_path)

    os.listdir(os.path.join(os.getcwd(), "cache"))


# ----------------------------------------------------------------------------------------------------------------------------


def cached_files():
    dir_contents = os.listdir("/Users/Martijn/Documents/Winc/files/cache/")
    file_list = []
    for entry in dir_contents:
        fullPath = os.path.join("/Users/Martijn/Documents/Winc/files/cache/", entry)
        if os.path.isdir(fullPath):
            pass
        else:
            file_list.append(fullPath)

    return file_list


# ----------------------------------------------------------------------------------------------------------------------------

file_list = cached_files()


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
        "/Users/Martijn/Documents/Winc/files/data.zip",
        "/Users/Martijn/Documents/Winc/files/cache",
    )
    cached_files()
    find_password(file_list)


# ----------------------------------------------------------------------------------------------------------------------------

# ik heb even een vraag bij de laatste functie: find_password.
# Ik heb een functie call gemaakt die er als volgt uitzag: find_password(*cached_files())
# Mijn funcie zag er dan als volgt uit;

# def find_password(*args):
#     for x in args:
#         openfile = open(x,'r')
#         line = openfile.readline()
#         while line != '':
#             line = openfile.readline()
#             if "password" in line:
#                 passkey = (line.replace("password: ", "").rstrip('\n'))
#                 return passkey

# Het password werd gegenereerd en ik kreeg geen errors. Alleen WINCPY accepteerde deze oplossing niet vanwege een TypeError.
# Maar zou dit niet een mooiere oplossing zijn, angezien ik de functie output van cached_files direct als argument kan gebruiken?

# ----------------------------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
