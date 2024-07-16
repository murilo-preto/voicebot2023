import speech_recognition as sr

def recognize_speech(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='pt-BR')
    except (sr.UnknownValueError, sr.RequestError) as e:
        print(f"Erro durante o reconhecimento de fala: {e}")
        return False