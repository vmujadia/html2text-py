import sys
import glob
import os


def write_file(path, content):
    create_folder("/".join(path.split('/')[:-1]))
    with open(path, 'w') as _file:
        for text in content:
            _file.write(text+'\n')
    print ('writting done at', path)

def list_all_html_files_from_folder(path):
    files = glob.glob(path + '/**/*.html', recursive=True)
    return files

def list_all_txt_files_from_folder(path):
    files = glob.glob(path + '/**/*.txt', recursive=True)
    return files

def create_folder(path):
    os.makedirs(path, exist_ok=True)
    print ('path created : ',path)
