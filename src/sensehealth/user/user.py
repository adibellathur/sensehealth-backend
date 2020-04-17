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

    def update_user_evaluation(self, data):
        """Send checkup taken from phone, parses it, and sends to db."""
        timestamp = str(int(time.time()))
        self._db_handler.put(
            ['user_data', self._user_id, 'evaluations'],
            {timestamp: data[evaluation}])
        )
        return

    def fetch_user_data(self, sensors, start_time):
        """Fetch data on user from db."""
        data = {}
        factory = SensorFactory()
        for s in sensors:
            sensor = factory.get_sensor(s, self._user_id, self._db_handler)
            data[s] = sensor.fetch_data(start_time)
        return data

    def add_group(self, group_id, group_name):
        """Add group to user's known groups."""
        self._db_handler.put(
            ['user_data', self._user_id, 'groups', group_id],
            group_name,
            auto_id=False
        )
        return

    def fetch_user_groups(self):
        """Get groups user is an admin for."""
        data = self._db_handler.get(['user_data', self._user_id, 'groups'])
        return data
