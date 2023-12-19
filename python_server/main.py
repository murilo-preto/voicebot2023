from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/pi')
def get_pi():
    return {'pi': 3.14159}

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)