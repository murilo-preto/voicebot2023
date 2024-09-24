
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token
from flask_cors import CORS
import re

from public.python.chatbot import chatbot
from public.python.textToSpeech import gtts_audio_var
from public.python.typeConversion import bytes_2_B64_string
from public.python.sqlFunctions import validar_login_server_hash

app = Flask(__name__)

# JWT access management
app.config['JWT_SECRET_KEY'] = '12345'
jwt = JWTManager(app)

# Enable cors
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/api/test_response', methods=['GET'])
def test_response():
    return 'Working as expected', 200

@app.route('/api/login', methods=['POST'])
def login():
    if request.form:
        data = request.form.to_dict()
        uname_cpf = data["username"]
        senha = data["password"]

        cpf = re.sub(r'[.-]', '', uname_cpf)
        print(f'{cpf}:{senha}')

        result, message = validar_login_server_hash(cpf, senha)
        print(result, message)

        if result:
            access_token = create_access_token(identity='admin')
            return jsonify(access_token=access_token), 200
        else:
            return jsonify(message='Credenciais recusadas.'), 401
    else:
        return jsonify(message='Empty request form'), 401

@app.route('/api/chatbot', methods=['POST'])
def chatbot_server():
    token = request.headers['token']
    username = request.headers['username']

    if request.form:
        data = request.form.to_dict()
        text = data["texto"]
        print(f'{username}: {text}')

        resposta = None
        if text!='':
            resposta = chatbot(token=token, username=username, input_text=text)
        else:
            resposta = 'Não entendi o que foi dito, repita a frase por favor.'

        # Gerar áudio da resposta
        audio_bytes = gtts_audio_var(resposta)
        base64_string = bytes_2_B64_string(audio_bytes)

        response_data = {
            'audio': base64_string,
            'text': resposta
        }

        return jsonify(response_data), 200