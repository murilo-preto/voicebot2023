# https://gtts.readthedocs.io/en/latest/module.html#languages-gtts-lang

from gtts import gTTS

if True:
    texto = "Bom dia, este é um teste para geração de texto em voz. Sim. Não."
else:
    texto = input("Digite o texto para ser convertido em voz: ")

tts = gTTS(texto, lang='pt', tld='com.br')
tts.save('test.mp3')