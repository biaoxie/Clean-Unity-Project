import os
import shutil

cwd = os.getcwd()
folders_to_keep = ["Assets", "Library", "ProjectSettings","Packages", "clean.py"]


def validate_path():
    files = os.listdir(cwd)
    if files.__contains__("Assets"):
        return True
    return False


def remove_folders():
    files = os.listdir(cwd)
    for file in files:
        if not folders_to_keep.__contains__(file):
            delete_file(cwd, file)


def clean_library():
    key = ".asset"
    libraryPath = os.path.join(cwd, folders_to_keep[1])
    files = os.listdir(libraryPath)
    for file in files:
        if not file.__contains__(key):
            delete_file(libraryPath, file)


def delete_file(pathName, name):
    fullName = os.path.join(pathName, name)
    if os.path.isdir(fullName):
        shutil.rmtree(fullName)
    else:
        os.remove(fullName)


if __name__ == '__main__':

    if not validate_path():
        print("Not a Valid Unity Project")
        exit(0)
    else:
        remove_folders()
        clean_library()
