from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Teste para GET
@app.route('/api/pi')
def get_pi():
    return {'usuario': 'murilo'}

# Rota post para lidar com Login
@app.route('/api/login', methods=['POST'])
def login():
    uname = request.form.get('uname')
    psw = request.form.get('psw')

    print(f'{uname}:{psw}')

    return "Success", 202

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)