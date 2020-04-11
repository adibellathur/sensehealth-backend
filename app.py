"""The main application that runs flask server."""

import json
from flask import Flask, request

app = Flask(__name__)


@app.route('/test_frontend', methods=['GET'])
def test_frontend():
    """Testing function for frontend."""
    return json.dumps({"key": "value"})


@app.route('/deposit_data', methods=['POST'])
def deposit_data():
    """Temporary endpoint to print sensor values. Must send JSON Object."""
    data = request.get_json(force=True)
    print(data)
    return data

@app.route('/')
def index():
    """Root endpoint. Currently for testing."""
    return "<h1>SenseHealth's Backend</h1>Check out: \
        https://5e9123ecf2fcfcdeef9cb85e--naughty-perlman-a4541f.netlify.com/"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
