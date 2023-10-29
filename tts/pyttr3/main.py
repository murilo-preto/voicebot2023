# https://pypi.org/project/pyttsx3/

import pyttsx3

# Init model
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