from os import (
    mkdir,
    getcwd,
    chdir,
    rename,
    remove,
    makedirs,
    listdir
)
from os.path import (
    abspath,
    isdir,
    isfile,
    exists,
    dirname,
    basename,
    join as os_join,
    split,
    getsize,
    relpath,
    samefile
)
from shutil import (
    rmtree,
    move,
    copy,
    copy2,
    copytree
    )
from .utils import make_filename_safe, hbs


class FileManager:
    @staticmethod 
    def remove(file_or_directory):
        if isfile(file_or_directory):
            remove(file_or_directory)
        elif isdir(file_or_directory):
            rmtree(file_or_directory)
    def mkdir(name):
        name=make_filename_safe(name) 
        #if not isdir(name)