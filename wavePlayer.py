import PySimpleGUI as sg
import simpleaudio as sa

#sg.theme('BluePurple')

# Loads the GUI
layout = [[sg.Text('FileName: '), sg.Text(size=(50,1)), sg.FileBrowse()],
          [ sg.Text('Status: '), sg.Text("BROWSE TO LOAD A FILE", size=(50,1), key='State')],
          [sg.Button('Play'), sg.Button('Stop'), sg.Button('Exit')]]

window = sg.Window('WAVE Player', layout)

# Event Loop
while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

    elif event == 'Play':
        try:
            window['State'].update("PLAYING")
            sa.stop_all()  
            waveObj = sa.WaveObject.from_wave_file(values['Browse'])
            play_obj = waveObj.play()

        except FileNotFoundError:
            window['State'].update("FILE NOT FOUND")

        except ValueError:
            window['State'].update("Weird sample rates are not supported, try another wave file")

        except Exception:
            window['State'].update("Does not appear to be a WAVE file, try another")
        
    elif event == 'Stop':
        try:
            sa.stop_all()
            window['State'].update("STOPPED")

        except NameError:
            window['State'].update("STOPPED")

window.close()