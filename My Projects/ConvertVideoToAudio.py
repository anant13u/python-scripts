# Python code to convert video to audio

import PySimpleGUI as sg
# from pathlib import Path
import os
import time
import subprocess
import moviepy.editor as mp # Before this the moviepy module needs to be installed using PIP

# sg.theme('Reddit')
sg.theme('darkgreen7')
sg.set_options(font=("Helvetica", 11))

layout = [  [sg.FileBrowse('Select Video',key='input-video',pad=(30,20)), sg.B('Convert to Audio'), sg.B('Exit',pad=(30,20))],
            [sg.T(key='file_display', pad=10)]  ]

Window = sg.Window('Video -> Audio by AU', layout, grab_anywhere=True, keep_on_top=True)


while True:
    event, values = Window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    if event=='Convert to Audio':
        try:
            inputVideo = values['input-video']
            Window['file_display'].update(inputVideo)
            outputFolder = os.path.dirname(inputVideo)
            print(f'outputFolder is {outputFolder}')
            print(f'Selected file name is {os.path.basename(inputVideo)}')
            outputAudio = inputVideo.replace('.mp4', '.mp3')
            # print(our_clip)
            our_clip=mp.VideoFileClip(inputVideo)
            audio_codecs = our_clip.audio.get_audio_codec()
            print(audio_codecs)            # our_clip.audio.write_audiofile(outputAudio)
            our_clip.audio.write_audiofile(outputAudio, codec='mp3')
            if subprocess.os.name == 'nt':  # Check if the platform is Windows
                subprocess.Popen(f'explorer {outputFolder}')
                # print(subprocess.Popen(r'explorer outputFolder'))
            else:  # For non-Windows platforms (e.g., Linux, macOS)
                subprocess.Popen(['xdg-open', outputFolder])
        except Exception as e:
            sg.popup_error(f'Error: {e}',keep_on_top=True)
            print(e)


# /home/anant/new
# "C:/Users/AU/Videos/InfraSound - Starlight   Epic Powerful Hybrid Orchestral Music.mp4"
