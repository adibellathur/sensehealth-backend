"""ECG Sensor Handler."""
from .sensor import Sensor


class ECGSensor(Sensor):
    """Class to handle ECG sensor data."""

    def __init__(self, user_id, db_handler):
        """Construct object."""
        super().__init__(user_id, db_handler)
        return

    def parse_data(self, data, timestamp, send_to_db=True):
        """Parse JSON for relevant data."""
        # TODO: parse the data to include only useful things
        if self._user_id and send_to_db:
            self._db_handler.put([
                'user_data',
                self._user_id,
                'ecg_sensor',
                timestamp
            ], data, auto_id=False)
        return data

    def fetch_data(self, timeframe):
        """Fetch data from database."""
        return {}
