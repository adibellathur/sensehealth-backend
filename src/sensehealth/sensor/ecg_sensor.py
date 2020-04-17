"""ECG Sensor Handler."""
import time
import random
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
        parsed = {}
        parsed["HR"] = sum(data["HR"]) / len(data["HR"])
        parsed["PatchId"] = data["PatchId"]
        parsed["ECG_CH_A"] = data["ECG_CH_A"]
        parsed["ECG_CH_B"] = data["ECG_CH_B"]
        parsed["LeadStatus"] = data["LeadStatus"]
        parsed["temp"] = random.uniform(96.0, 101.0)
        parsed["pulse_oximeter"] = random.uniform(0.93, 0.99)
        if self._user_id and send_to_db:
            self._db_handler.put([
                'user_data',
                self._user_id,
                'ecg_sensor',
                timestamp
            ], parsed, auto_id=False)
        return parsed

    def fetch_data(self, start_time):
        """Fetch data from database."""
        data = None
        if start_time == "-1":
            data = self._db_handler.get(
                ['user_data', self._user_id, 'ecg_sensor'],
                sort_by_key=True,
                limit_to_last=1
            )
        else:
            timestamp = str(int(time.time()))
            data = self._db_handler.get(
                ['user_data', self._user_id, 'ecg_sensor'],
                sort_by_key=True,
                in_range=[start_time, timestamp]
            )
        return data
