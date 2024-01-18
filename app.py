"""
# Folder Handeling

Receber o endereço da pasta que desejamos acessar pra converter os vídeos (input_folder)

Mudar o processo para esta pasta (caso não exista, apontar erro)

Pedir pasta de saída para os vídeos (se não for digitado, converter os vídeos para a pasta de origem e apagar os vídeos de entrada)

Perguntar se deseja apagar os vídeos de origem (caso exista uma pasta de saída)

Rodar função de conversão dos vídeos
"""
import os
from converter import convert_video_to_mp4


def converting(output_folder):
    video_list = os.listdir('.')
    for video in video_list:
        output = output_folder + '\\' + video.replace('AVI', 'MP4')
        convert_video_to_mp4(video, output)

def folder_handling():
    while True:
        error = False
        print('Type the output folder: ')
        output_folder = input()
        output_folder.replace('\\', '/')
        try:
            os.listdir(path=output_folder)
        except OSError:
            error = True
        
        if not error:
            converting(output_folder)
            break


def run_app():
    while True:
        print('Type the desired folder to get the AVI videos to convert: ')
        print('Type X if you want to finish the run process')
        input_folder = input()
        match input_folder:
            case 'X':
                break
            case _:
                error = False
                try:
                    os.chdir(input_folder)
                except OSError:
                    error = True

                if not error:
                    folder_handling()
                    break
