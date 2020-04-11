"""Handler for Database Operations."""
import pyrebase
from datetime import datetime


class DBHandler(object):
    """Handles all Firebase interactions."""

    def __init__(self, config):
        """Construct object."""
        self.db = pyrebase.initialize_app(config).database()
        return

    def __find_collection(self, collection_path):
        collection = self.db
        for c in collection_path:
            collection = collection.child(c)
        return collection

    def test_db(self, json):
        """Tests Access to DB."""
        self.db.child("raw_sensor_data").push({
            "sensor_type": "testing - {}".format(datetime.now().time()),
            "json_data": json
        })
        return

    def put(self, collection_path, data, auto_id=False):
        """
        Put data into the firebase db.

        Args:
            collection_path (list[str]): a list of nested children to enter
                before putting data into db.
            data (dict): json object with data to put into db.
            auto_id: Whether or not to use an auto_id for the data or if key is
                present already in the data dict.
        """
        collection = self.__find_collection(collection_path)
        if auto_id:
            collection.push(data)
        else:
            collection.set(data)
        return
