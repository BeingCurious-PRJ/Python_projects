import os
import json
import uuid
from pathlib import Path


def get_key_value(file_path):
    value_file = r'path of the file on the local folder where new key value for each json file exists'  # replace the path with the path of the file on the local folder
    [_, f_name] = os.path.split(file_path)
    with open(value_file) as f:
        my_list = [line.split('=') for line in f.read().splitlines()]
    for values in my_list:
        if f_name in values[0]:
            new_hash = values[1]
            return new_hash


def update_key_value(file):
    with open(file) as f:
        key_value = get_key_value(file)  # function call to get the matching hash
        data = json.load(f)
        data['schema hash'] = key_value  # the 'schema hash' could be any key name in json files that you want to change
    temp = os.path.join(os.path.dirname(file), str(uuid.uuid4()))
    with open(temp, 'w') as f:
        json.dump(data, f, indent=4)
    os.replace(temp, file)


if __name__ == '__main__':
    path_list = Path(str(r'path with the folder where the json files exists')).rglob(
        '*.json')  # replace the path with the folder where the json files exists

    for files in path_list:
        filename = str(files)
        # print(filename)
        update_key_value(filename)  # function to update the new schema hash
