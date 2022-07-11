# -*- coding: utf-8 -*-
"""
All You need for the GUI
1.Elements & Layout
2.Events & Values
3.Update

"""

import PySimpleGUI as sg

def matchingvalues(string,value):
    case = {
        1: 'km to miles',
        2: 'kg to punds'
        }
    case.get(string)
    if case == 1 :
        output = float(value) * 0.6214 
    print (output)  
    
    
    
layout=[
        [sg.Input(key='-INPUT1-'),
         sg.Spin(['km to miles',
                  'kg to punds'],key='-UNIT1-'),
         sg.Button('Convert', key = '-BUTTON1-' )
        ],
        [sg.Text('Output', key = '-OUTPUT-')]
]

window = sg.Window("Converter",layout)


       
while True:
    #read the Events(text,button, etc..) and values(input,spin,etc..)
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
    
    
    input_spin = values['-UNIT1-']
    
    if event == '-BUTTON1-':
        input_value = values['-INPUT1-']
        
        if input_value.isnumeric():
           #check the spin to convert 
           if input_spin =='km to miles' :
               output = float(input_value) * 0.6214 
               output_string = f'{input_value} km are {output} miles.'
               
           elif input_spin == 'kg to punds':
               output = float(input_value) * 2.2046
               output_string = f'{input_value} kg are {output} punds.'
               
              
                    
           window['-OUTPUT-'].update(output_string)    
            
           

window.close()    