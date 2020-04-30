from flask import Flask, jsonify, request, Response
from flask_cors import CORS
import datetime
from src.use_cases import load_use_cases

app = Flask(__name__, static_url_path='')
CORS(app)

API_V1 = '/api/v1'

use_cases = load_use_cases('./models.json')

@app.route(API_V1 + '/ping', methods=['GET'])
def ping() -> Response:
    return "pong"

@app.route(API_V1 + '/info', methods=['GET'])
def info() -> Response:
    return jsonify({
        'version': API_V1,
        'project': '5 elements of AI',
        'service': 'backend',
        'language': 'python',
        'type': 'api',
        'date': str(datetime.datetime.now())
    })


@app.route(API_V1 + '/use-cases', methods=['GET'])
def usecases() -> Response:
    return jsonify({
        'use_cases': use_cases
    })


@app.route(API_V1 + '/use-cases/<use_case>/predict')
def predict(use_case: str) -> Response:
    use_case = use_cases[use_case]
    
    data = request.get_json()
    
    prediction = use_case.predict_json(data)
    return jsonify(prediction)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)
