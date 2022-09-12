import os
import json
import uuid
from pathlib import Path
import subprocess


def generate_hash_keys():
    key_list = []
    for file in path_list:
        file_name = str(file)
        os.chdir('C:\\')
        cmnd = "certutil -hashfile " + file_name + " sha512"
        cmd_output = subprocess.check_output(cmnd, shell=True, universal_newlines=True)
        out_split = cmd_output.split(":")
        [_, path_tail] = os.path.split(out_split[1])
        key_list.append(path_tail)
        print(path_tail)
        key = out_split[2].split()
        key_list.append(key[0])
    return key_list


def get_new_sha512_content(key_list):
    with open(sha_file) as f:
        my_list = [line.split('=') for line in f.read().splitlines()]
    for schemas in my_list:
        for i in range(8):
            if key_list[i] in schemas[0]:
                new_hash = key_list[i + 1]
                schemas[1] = new_hash
    my_list = [ele for ele in my_list if ele != ['']]
    return my_list


def modify_sha512_file(new_sha_keys):
    with open(sha_file, 'w') as fl:
        for item in new_sha_keys:
            new_item = "="
            new_item = new_item.join(item)
            print(new_item)
            fl.write("%s\n" % new_item)


if __name__ == '__main__':
    path_list = Path(str(r'path with the folder where the json files exists')).rglob(
        '*.json')  # replace the path with the folder where the json files exists
    sha_file = r'path of the SHA512 file on the local folder to update new hash corresponding to each json filename'
    list_key = generate_hash_keys()
    new_shaKeys = get_new_sha512_content(list_key)
    modify_sha512_file(new_shaKeys)

