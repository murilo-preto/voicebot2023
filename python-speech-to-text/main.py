import speech_recognition as sr

audio_file = "audio.wav"

def recognize_speech(file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(file_path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_google(audio, language='pt-BR')
    except (sr.UnknownValueError, sr.RequestError) as e:
        raise ValueError(f"Erro durante o reconhecimento de fala: {e}")

try:
    text = recognize_speech(audio_file)
    print("Você disse:", text)
except ValueError as e:
    print(e)