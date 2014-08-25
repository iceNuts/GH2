import json
import os

def read_file(path):
    f = open(path)
    raw = f.read()
    f.close()
    return raw

def read_folder(path):
    raw = ""
    for dir_entry in os.listdir(path):
        dir_entry_path = os.path.join(path, dir_entry)
        if os.path.isfile(dir_entry_path):
            with open(dir_entry_path, 'r') as my_file:
                raw += my_file.read()
                my_file.close()
    return raw

def read_json(path):
    f = open(path)
    return json.load(f)