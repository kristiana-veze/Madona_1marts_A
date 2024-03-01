import PySimpleGUI as sg
import os

layout = [[sg.Text("Ievadiet vārdu"), sg.InputText(key="--vards--")],
           [sg.Text("Ievadiet uzvārdu"), sg.InputText(key="--uzvards--")],
           [sg.Multiline(size=(50, 10), key='--vieta--', disabled=True)],
           [sg.Button('Drukāt')]]

loggs=sg.Window("EGLE", layout, background_color='#FFD1DC')

saturs=input

while True:
    event, values=loggs.read()

    if event == sg.WINDOW_CLOSED or event == 'Iziet':
        break
    elif event=="Drukāt":
        vards=values['--vards--']
        uzvards=values['--uzvards--']
        asd=(vards,uzvards)
        asd.save('es.txt')
        loggs['--vieta--'].update('Labdien,{vards} {uzvards}!')
loggs.close()