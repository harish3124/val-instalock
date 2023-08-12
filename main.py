import PySimpleGUI as sg
from logic import *

import random

import json
agents = json.load(open("agents.json")).keys()
agents = list(agents)

# sg.theme('DarkPurple1')
sg.theme('DarkBlue')
layout = [  [sg.Text("Mode:"), sg.Combo(["Agent Select", "Random Agent"], enable_events=True, readonly=True, key="mode_select")],
            [sg.Text("Agent:"), sg.Combo(agents, visible=False, enable_events=True, readonly=True, key="agent_list")],
            [sg.Button('Start', visible=False, border_width=0), sg.Button('Stop', visible=False, border_width=0)] ]

window = sg.Window('Window Title', layout, size=(300,200))

run_locker = False
while True:
    event, values = window.read(timeout=200)
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    if event == "mode_select":
        selected_mode = values[event]
        window["agent_list"].update(visible=(selected_mode == "Agent Select"))
        
        if selected_mode == "Random Agent":
            selected_agent = random.choice(agents)
            window["Start"].update(visible=True)
        else:
            window["Start"].update(visible=False)
    
    if event == "agent_list":
        window["Start"].update(visible=(values[event] in agents))
        selected_agent = values[event]

    if event == "Start":
        window["Start"].update(visible=False)
        window["Stop"].update(visible=True)
        run_locker = True
    
    if event == "Stop":
        window["Stop"].update(visible=False)
        window["Start"].update(visible=True)
        run_locker = False
    
    if run_locker:
        locker(selected_agent)
    
window.close()
exit()