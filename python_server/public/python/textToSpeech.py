# from gtts import gTTS
# https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

# def gtts_tts(texto):
#     if True:
#         texto = "Bom dia, este é um teste para geração de texto em voz. Sim. Não."
#     else:
#         texto = input("Digite o texto para ser convertido em voz: ")

#     tts = gTTS(texto, lang='pt', tld='com.br')
#     tts.save('reponseAudio.mp3')

import pyttsx3
# https://pypi.org/project/pyttsx3/

def pyttr3_tts(texto, outputPath):
    try:
        speaker = pyttsx3.init()

        speaker.setProperty('voice', 'brazil')
        rate = speaker.getProperty('rate')
        speaker.setProperty('rate', rate - 70)

        print(f'TTS: Texto a ser convertido: {texto}')
        print(f'TTS: Caminho de saída: {outputPath}')

        speaker.save_to_file(texto, outputPath)
        speaker.runAndWait()
    except Exception as e:
        print(e)
