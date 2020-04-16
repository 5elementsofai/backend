from flask import Flask, jsonify
from flask_cors import CORS
import datetime

app = Flask(__name__, static_url_path='')
CORS(app)

API_V1 = '/api/v1'


@app.route(API_V1 + '/ping', methods=['GET'])
def ping():
    return jsonify({
        'version': API_V1,
        'project': '5 elements of AI',
        'service': 'backend',
        'language': 'python',
        'date': str(datetime.datetime.now())
    })
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3030, debug=False, threaded=True)
