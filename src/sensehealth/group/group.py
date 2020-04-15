"""Group class to handle group information."""
from ..user.user import User

class Group(object):
    """Class to handle individual group actions."""

    def __init__(self, group_id, db_handler):
        """Construct object."""
        self._group_id = group_id
        self._db_handler = db_handler
        return

    def get_group_data(self, sensors, start_time):
        """Fetch Sensor Data for all users in Group."""
        data = {}
        response = self._db_handler.get(['group_data', self._group_id])
        if not response:
            print("ERROR: Group Not Found")
            return None

        data['group_info'] = response
        data['members'] = {}
        for mem in response['members']:
            user_data = User(mem, self._db_handler).fetch_user_data(
                sensors,
                start_time
            )
            data['members'][mem] = user_data
        return data
