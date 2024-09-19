from os import popen
from pathlib import Path

command = r"""uuid=$(uuidgen); sed -i '0,/---\n/{s/---\n/---\nuuid: '"$uuid"'\n/}' """

def recur_find_md_files(path):
    for p in path.iterdir():
        if p.is_dir():
            recur_find_md_files(p)
        elif p.suffix == '.md':
            popen(command + '"' + str(p) + '"')

recur_find_md_files(Path('.'))
