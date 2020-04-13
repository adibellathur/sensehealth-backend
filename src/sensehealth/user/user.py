"""User class to handle updating and fetching a users data."""
import time

from ..sensor.sensor_factory import SensorFactory


class User(object):
    """User class to handle updating and fetching a users data."""

    def __init__(self, user_id, db_handler):
        """Construct user with key data."""
        self._user_id = user_id
        self._db_handler = db_handler
        return

    def update_user_data(self, data):
        """Send data taken from phone, parses it, and sends to db."""
        timestamp = str(int(time.time()))
        factory = SensorFactory()
        for key in data:
            if key != "user_id":
                sensor = factory.get_sensor(
                    key,
                    self._user_id,
                    self._db_handler
                )
                if sensor:
                    sensor.parse_data(data[key], timestamp, send_to_db=True)
        return
