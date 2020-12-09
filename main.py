import tkinter as tk
from tkinter import filedialog

import PySimpleGUI as sg
from serialization import save_project, open_project

root = tk.Tk()
root.withdraw()

# Define menu
menu_def = [ 
             ['&File', ['&Open', '&Save', '&Exit',]],
             ['Export', ['Render', ['To MP4', 'To MPEG', 'To WEBP', 'To MOV',], ],],
           ]

# Define the window's contents
layout = [  
            [sg.Menu(menu_def)],
            [sg.Text("Project Name: ")],
            [sg.Input(key="__PROJECT_NAME__")],
            [sg.FilesBrowse('Import Clips', target='clipspaths', file_types=(("MP4 files", "*.mp4"), ("MPEG files", "*.mpeg"), ("MOV files", "*.mov"))), sg.Input(disabled=True, enable_events=True, key="clipspaths")],
            [sg.Listbox(values=[], enable_events=True, size=(40,20), key='clipslist'), sg.Button(">", key="import"), sg.Listbox(values=[], enable_events=True, size=(40,20), key='clipslistordered')]
         ]


# Create the window
window = sg.Window('Window Title', layout)

project = {
    "project_name": "",
    "file_name": "",
    "imported_clips": [],
}

selected_clip = ""
all_clips = []
imported_clips = []

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'Save':
        project["project_name"] = values["__PROJECT_NAME__"]
        save_project(project)
        sg.Save()
    if event == 'Open':
        file_path = filedialog.askopenfilename(filetypes = (("qVEW File", "*.qvew"), ("All files", "*")))
        project = open_project(file_path)
        
        window['clipslistordered'].update(project["imported_clips"])
        window['__PROJECT_NAME__'].update(project["project_name"])
        selected_clip = ""

    if event == 'clipspaths':
        fnames = (values['clipspaths']).split(";")
        all_clips = fnames
        window['clipslist'].update(fnames)
    if event == 'clipslist':
        selected_clip = values['clipslist'][0]
    if event == 'import' and len(selected_clip) > 0:
        all_clips.remove(selected_clip)
        window['clipslist'].update(all_clips) # REMOVE FROM CURRENT LIST

        project["imported_clips"].append(selected_clip) # ADD TO IMPORTED LIST
        window['clipslistordered'].update(project["imported_clips"])
        selected_clip = ""


# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
