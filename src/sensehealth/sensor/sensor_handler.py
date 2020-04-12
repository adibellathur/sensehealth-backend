"""Parent class for all handlers of sensor data."""
from abc import ABC, abstractmethod


class SensorHandler(ABC):
    """Abstract Class to set structure of how to handle sensor data."""

    def __init__(self, db_handler):
        """Construct object."""
        self.db_handler = db_handler
        return

    @abstractmethod
    def parse_json(self, data, send_to_db=True):
        """Parse JSON for relevant data"""
        pass

    @abstractmethod
    def fetch_data(self, username):
        """fetches data from database."""
        pass
