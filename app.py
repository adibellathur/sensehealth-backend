"""The main application that runs flask server."""

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """Main endpoint. Currently for testing."""
    return "<h1>SenseHealth's Backend</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
