"""Parent class for all handlers of sensor data."""
from abc import ABC, abstractmethod


class Sensor(ABC):
    """Abstract Class to set structure of how to handle sensor data."""

    @abstractmethod
    def __init__(self, user_id, db_handler):
        """Construct object."""
        self._db_handler = db_handler
        self._user_id = user_id
        return

    @abstractmethod
    def parse_data(self, data, timestamp, send_to_db=True):
        """Parse JSON for relevant data."""
        pass

    @abstractmethod
    def fetch_data(self, timeframe):
        """Fetch data from database."""
        pass
