"""Factory to get the correct sensor handler class."""
from .ecg_sensor import ECGSensor


SENSOR_IDS = [
    "ecg_sensor",
    "heart_sensor",
    "oxygen_sensor"
]


class SensorFactory(object):
    """Factory class to give correct sensor child object from id."""

    def __init__(self):
        """Construct Object."""
        return

    def get_sensor(self, sensor_id, user_id, db_handler):
        """Get correct sensor object from id."""
        sensor = None
        if sensor_id == SENSOR_IDS[0]:
            sensor = ECGSensor(user_id, db_handler)
        elif sensor_id == SENSOR_IDS[1]:
            pass
        elif sensor_id == SENSOR_IDS[2]:
            pass
        else:
            print('INVALID SENSOR TYPE: {}'.format(sensor_id))
            print('Supported types: {}'.format(SENSOR_IDS))
        return sensor
