import PySimpleGUI as sg
import simpleaudio as sa

sg.theme('BluePurple')
layout = [[sg.Text('Culex.wav: '), sg.Text(size=(15,1), key='-STATE-')],
          [sg.Button('Play'), sg.Button('Stop'), sg.Button('Exit')]]
window = sg.Window('MP3 Player', layout)

waveObj = sa.WaveObject.from_wave_file("./culex.wav")

while True:
    event, values = window.read()
    print(event, values)
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event == 'Play':
        play_obj = waveObj.play()
        window['-STATE-'].update("PLAYING")
    if event == 'Stop':
        try:
            play_obj.stop()
            window['-STATE-'].update("STOPPED")
        except NameError:
            window['-STATE-'].update("STOPPED")


    
window.close()