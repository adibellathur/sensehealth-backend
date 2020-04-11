"""Handler for Database Operations."""
import pyrebase
from datetime import datetime


class DBHandler(object):
    """Handles all Firebase interactions."""

    def __init__(self, config):
        """Construct object."""
        self.db = pyrebase.initialize_app(config).database()
        return

    def test_db(self, json):
        """Tests Access to DB."""
        self.db.child("raw_sensor_data").push({
            "sensor_type": "testing - {}".format(datetime.now().time()),
            "json_data": json
        })
        return
