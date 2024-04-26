from gtts import gTTS
# https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

def gtts_tts(texto, wavOutputPath):
    '''
    Conversão de texto em áudio com saída .WAV
    '''

    tts = gTTS(texto, lang='pt', tld='com.br')
    tts.save(wavOutputPath)

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

gtts_tts('texto', 'audio.wav')