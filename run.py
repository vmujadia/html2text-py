import sys
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import utils

lab_name = sys.argv[1]
lab_folder_path = sys.argv[2]


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def get_text_content_from_html(path):
    html = open(path,'r').read()
    soup = BeautifulSoup(html,"html.parser")

    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    text = text.split('\n\t')
    text = " ".join(text)
    send = []
    
    for ty in text.split('\n'):
        ty=ty.strip()
        ty = " ".join(ty.split())
        if ty:
            send.append(ty)
    return send

files = utils.list_all_html_files_from_folder(lab_folder_path)

for _file in files:
    print ('for file:',_file)
    file_path = os.path.join(lab_name, _file.split(lab_folder_path)[1])
    text = get_text_content_from_html(_file)
    utils.write_file(file_path.replace('html','txt'), text)

#for t in get_text_content_from_html(sys.argv[3]):
#    print (t)
