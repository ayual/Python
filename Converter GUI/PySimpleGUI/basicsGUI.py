# -*- coding: utf-8 -*-
"""
All You need for the GUI
1.Elements & Layout
2.Events & Values
3.Update

"""

import PySimpleGUI as sg



layout=[
        [sg.Text("Text", enable_events= True , key = '-TEXT-'),sg.Spin(["item1","item2"])],
        [sg.Button("Button", key = "-BUTTON1-" )],
        [sg.Input(key='-INPUT-')],
        [sg.Text("Text2"),sg.Button("Button", key = "-BUTTON2-" )],
]

window = sg.Window("converter",layout)


while True:
    #liest die Events(text,button, etc..) und values(input,spin,etc..)
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    if event == "-BUTTON1-" :
        #update kann den default wert ändern im GUI 
        window['-TEXT-'].update(visible = False)
        #print(values['-INPUT-']) # Gibt nur den Input aus
        
    if event == "Button2" :
        print("button2 presed")
    
    if event == '-TEXT-' :
        print('You pressed The Text')
        
window.close()    