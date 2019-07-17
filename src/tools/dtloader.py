from json import load
from os import path


def read_json(project_root,
              target_file,
              json_key=None):
    with open(path.join(project_root,
                        '../' + target_file)) as json_file:
        file_content = load(json_file)
    if json_key is not None:
        return file_content[json_key]
    return file_content
