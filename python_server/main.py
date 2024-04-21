from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS
import base64
import tempfile
import os
from public.python.webm2wav import webm_to_wav_ffmpeg
from public.python.speechToText import recognize_speech
from public.python.textToSpeech import pyttr3_tts

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '12345'
jwt = JWTManager(app)
CORS(app)

@app.route('/api/login', methods=['POST'])
def login():
    if request.form:
        data = request.form.to_dict()
        uname = data["username"]
        psw = data["password"]
        print(f'{uname}:{psw}')

        if uname!=None:
            access_token = create_access_token(identity=uname)
            return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Empty request form'), 401 
    
@app.route('/api/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return 'Nenhum arquivo de áudio enviado', 400

    audio_file = request.files['audio']
    text = None

    with tempfile.NamedTemporaryFile(suffix='.webm', delete=False) as tmp_webm_audio:
        temp_webm_audio_path = tmp_webm_audio.name
        audio_file.save(temp_webm_audio_path)

        with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as tmp_wav_audio:
            temp_wav_audio_path = tmp_wav_audio.name
            webm_to_wav_ffmpeg(temp_webm_audio_path, temp_wav_audio_path)

            text = recognize_speech(temp_wav_audio_path)

    temp_file_descriptor, temp_file_name = tempfile.mkstemp(suffix=".mp3")
    os.close(temp_file_descriptor)

    temp_mp3_audio_path = temp_file_name
    pyttr3_tts(text, temp_mp3_audio_path)

    with open(temp_mp3_audio_path, 'rb') as mp3_file:
        audio_content = mp3_file.read()

    audio_base64 = base64.b64encode(audio_content).decode('utf-8')

    response_data = {
        'audio': audio_base64,
        'text': text
    }

    os.remove(temp_webm_audio_path)
    os.remove(temp_wav_audio_path)
    os.remove(temp_mp3_audio_path)

    return jsonify(response_data), 200

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
