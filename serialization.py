from yaml import dump, load, Loader

import re

def get_filename(project_template):
    filename = project_template["project_name"]
    filename = filename.replace(" ", "_")
    filename = filename.lower()
    filename = re.sub('[^\w\-_\. ]', '_', filename)
    return filename + ".qvew"

def open_project(filename):
    if len(filename) > 0:
        with open(filename, "r") as file:
            contents = file.read()
            return load(contents, Loader=Loader)


def save_project(project_template):
    project_template["file_name"] = str(get_filename(project_template))
    
    with open(project_template["file_name"], 'w') as file:
        contents = dump(project_template)
        file.write(contents)
