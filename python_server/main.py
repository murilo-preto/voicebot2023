from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)
CORS(app)

# Teste para GET
@app.route('/api/pi')
def get_pi():
    return {'usuario': 'murilo'}

# Rota post para lidar com Login
@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.get_json()
    uname = json_data.get('uname')
    psw = json_data.get('psw')

    print(f'{uname}:{psw}')
    if uname!=None: #Credentials OK
        access_token = create_access_token(identity=uname)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)