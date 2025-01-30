from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime, timezone

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_info():
    current_utc = datetime.utcnow().replace(microsecond=0)
    formatted_datetime = current_utc.isoformat() + 'Z'
    response = {
        "email": "victorcyrus01@gmail.com",
        "current_datetime": formatted_datetime,
        "github_url": "https://github.com/NjengaC/hnginternship"
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
