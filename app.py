"""The main application that runs flask server."""
import os
import json
from flask import Flask, request
from dotenv import load_dotenv
from flask_cors import CORS

from src.sensehealth.database.database_handler import DBHandler
from src.sensehealth.user.user import User
from src.sensehealth.group.group_manager import GroupManager
from src.sensehealth.group.group import Group

app = Flask(__name__)
CORS(app)

load_dotenv()
CONFIG = {
    "apiKey": "-none-",
    "serviceAccount": json.loads(os.environ['FIREBASE_API_KEY']),
    "authDomain": "{}.firebaseapp.com".format(os.environ['PROJECT_ID']),
    "databaseURL": "https://{}.firebaseio.com".format(os.environ['PROJECT_ID']),
    "storageBucket": "{}.appspot.com".format(os.environ['PROJECT_ID']),
}
db_handler = DBHandler(CONFIG)
group_manager = GroupManager(db_handler)


@app.route('/test_frontend', methods=['GET'])
def test_frontend():
    """Testing function for frontend."""
    return json.dumps({"key": "value"})


@app.route('/deposit_data', methods=['POST'])
def deposit_data():
    """
    Temporary endpoint to put JSON sensor values into database.

    NOTE: DO NOT USE ANYMORE.
    """
    req = request.get_json(force=True)
    db_handler.put(['raw_sensor_data'], req, auto_id=True)
    return req


@app.route('/fetch_all_data', methods=['GET'])
def fetch_all_data():
    """Temporary endpoint to print sensor values. NOTE: DO NOT USE ANYMORE."""
    sensor_data = db_handler.get(['raw_sensor_data'])
    return sensor_data


@app.route('/update_user_data', methods=['POST'])
def update_user_data():
    """Temporary endpoint to put JSON sensor values into database."""
    req = request.get_json(force=True)
    User(req['user_id'], db_handler).update_user_data(req)
    return req


@app.route('/update_user_evaluation', methods=['POST'])
def update_user_evaluation():
    """Temporary endpoint to put checkups into database."""
    req = request.get_json(force=True)
    User(req['user_id'], db_handler).update_user_evaluation(req)
    return req


@app.route('/fetch_user_data', methods=['GET', 'POST'])
def fetch_user_data():
    """Put user's JSON sensor values into database."""
    req = request.get_json(force=True)
    data = User(req['user_id'], db_handler).fetch_user_data(
        req['sensors'],
        str(req['start_time'])
    )
    if data:
        return data
    return {}


@app.route('/fetch_user_groups', methods=['GET', 'POST'])
def fetch_user_groups():
    """Put user's JSON sensor values into database."""
    req = request.get_json(force=True)
    data = User(req['user_id'], db_handler).fetch_user_groups()
    if data:
        return data
    return {}


@app.route('/create_group', methods=['POST'])
def create_group():
    """Create group in db."""
    req = request.get_json(force=True)
    data = group_manager.create_group(req)
    if data:
        return data
    return {}


@app.route('/fetch_group_data', methods=['GET', 'POST'])
def fetch_group_data():
    """Create group in db."""
    req = request.get_json(force=True)
    data = Group(req['group_id'], db_handler).get_group_data(
        req['sensors'],
        str(req['start_time'])
    )
    if data:
        return data
    return {}


@app.route('/')
def index():
    """Root endpoint. Currently for testing."""
    return "<h1>SenseHealth's Backend</h1>Check out: \
        https://5e9123ecf2fcfcdeef9cb85e--naughty-perlman-a4541f.netlify.com/"


if __name__ == '__main__':
    app.run(threaded=True, port=5000)
