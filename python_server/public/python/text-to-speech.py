from gtts import gTTS
# https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

import pyttsx3
# https://pypi.org/project/pyttsx3/

def gtts_tts(texto):
    if True:
        texto = "Bom dia, este é um teste para geração de texto em voz. Sim. Não."
    else:
        texto = input("Digite o texto para ser convertido em voz: ")

    tts = gTTS(texto, lang='pt', tld='com.br')
    tts.save('test.mp3')

def pyttr3_tts(texto):
    speaker=pyttsx3.init()

    # Set parameters, rate -> speaking speed
    speaker.setProperty('voice', 'brazil')
    rate = speaker.getProperty('rate')
    speaker.setProperty('rate', rate-50)

    if True:
        texto = "Bom dia, este é um teste para geração de texto em voz. Sim. Não."
    else:
        texto = input("Digite o texto para ser convertido em voz: ")

    speaker.save_to_file(texto, 'test.mp3')
    speaker.runAndWait()
