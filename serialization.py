from yaml import dump

import re

def get_filename(project_template):
    filename = project_template["project_name"]
    filename = filename.replace(" ", "_")
    filename = filename.lower()
    filename = re.sub('[^\w\-_\. ]', '_', filename)
    return filename + ".qvew"

def save_project(project_template):
    project_template["file_name"] = str(get_filename(project_template))
    
    with open(project_template["file_name"], 'w') as file:
        contents = dump(project_template)
        file.write(contents)
