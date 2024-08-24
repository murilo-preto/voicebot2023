from gtts import gTTS
# import pyttsx3
import io

def gtts_audio_var(text):
    '''
    Conversão de texto em áudio

    use: gtts_audio_var('texto para ser convertido')
    '''
    try:
        tts = gTTS(text=text, lang='pt')
        
        audio_buffer = io.BytesIO()
        tts.write_to_fp(audio_buffer)
        
        audio_buffer.seek(0)
        
        return audio_buffer
    except Exception as e:
        print(e)
        return None


# def gtts_tts_disk(texto, wavOutputPath):

#     tts = gTTS(texto, lang='pt', tld='com.br')
#     tts.save(wavOutputPath)

# def pyttr3_tts(texto, outputPath):
#     try:
#         speaker = pyttsx3.init()

#         speaker.setProperty('voice', 'brazil')
#         rate = speaker.getProperty('rate')
#         speaker.setProperty('rate', rate - 70)

#         print(f'TTS: Texto a ser convertido: {texto}')
#         print(f'TTS: Caminho de saída: {outputPath}')

#         speaker.save_to_file(texto, outputPath)
#         speaker.runAndWait()
#     except Exception as e:
#         print(e)