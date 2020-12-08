import PySimpleGUI as sg

# Define the window's contents
layout = [  
            [sg.Text("Project Name: ")],
            [sg.Input()],
            [sg.FilesBrowse('Import Clips', target='clipspaths', file_types=(("MP4 files", "*.mp4"), ("MPEG files", "*.mpeg"), ("MOV files", "*.mov"))), sg.Input(disabled=True, enable_events=True, key="clipspaths")],
            [sg.Listbox(values=[], enable_events=True, size=(40,20), key='clipslist')]
         ]


# Create the window
window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == 'clipspaths':
        fnames = (values['clipspaths']).split(";")
        print(fnames)
        window['clipslist'].update(fnames)


# Do something with the information gathered
print('Hello', values[0], "! Thanks for trying PySimpleGUI")

# Finish up by removing from the screen
window.close()
