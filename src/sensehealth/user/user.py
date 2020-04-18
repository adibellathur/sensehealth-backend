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
            {timestamp: data['evaluation']},
            auto_id=False
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

    def get_user_overview(self, sensors, start_time):
        """Make things."""
        data = {}
        factory = SensorFactory()
        for s in sensors:
            sensor = factory.get_sensor(s, self._user_id, self._db_handler)
            data[s] = sensor.get_data_overview(start_time)
        return data

    def get_user_evaluations(self):
        """Make things."""
        evals = {}
        curr_eval = self._db_handler.get(
            ['user_data', self._user_id, 'evaluations'],
            sort_by_key=True,
            limit_to_last=1
        )
        av_eval = self._db_handler.get(
            ['user_data', self._user_id, 'evaluations'],
            sort_by_key=True,
        )
        if av_eval:
            evals['average'] = []
            for key in av_eval:
                evals['average'].append(int(av_eval[key]))
            evals['average'] = sum(evals['average']) / len(evals['average'])
        if curr_eval:
            for key in curr_eval:
                evals['current'] = curr_eval[key]
        return evals
