from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = '12345'
jwt = JWTManager(app)
CORS(app)

# Rota post para lidar com Login
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

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)