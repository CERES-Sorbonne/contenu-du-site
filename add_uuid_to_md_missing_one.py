from os import popen
from pathlib import Path

command = r"""uuid=$(uuidgen); sed -i '0,/---/{s/---/---\nuuid: '"$uuid"'\n/}' """

def recur_find_md_files(path):
    for p in path.iterdir():
        if p.is_dir():
            recur_find_md_files(p)
        elif p.suffix == '.md':
            with open(p, 'r') as f:
                txt = f.read()
                # print(p)
                if txt.startswith('---\nuuid:'):
                    # print('uuid already exists in', p)
                    continue

            popen(command + '"' + str(p) + '"')
            print('uuid added to', p)

recur_find_md_files(Path('.'))
