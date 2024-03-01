import PySimpleGUI as sg

sg.change_look_and_feel('SystemDefault1')

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content=file.read()
            return content
    except Exception as e:
        return f"Ķļūda: {e}"

layout=[
        [sg.Text("Izvēlaties txt failu:")],
        [sg.InputText(key='filename'), sg.FileBrowse()],
        [sg.Button('Nolasīt'), sg.Button('Iziet')],
        [sg.Multiline(size=(50,10), key='output', disabled=True)]
    ]

window=sg.Window('Nolasīt teksta failu', layout)

def main():
    while True:
        event, values= window.read()

        if event== sg.WINDOW_CLOSED or event =='Iziet':
            break
        
        if event == 'Nolasīt':
            filename=values['filename']
            if filename:
                saturs=read_file(filename, skiprows=3)
                window['output'].update(saturs)

    

if __name__=="__main__":
    main()