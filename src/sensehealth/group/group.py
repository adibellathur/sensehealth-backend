"""Group class to handle group information."""
from ..user.user import User

class Group(object):
    """Class to handle individual group actions."""

    TEMP_THRESHOLD = 100.0
    OX_THRESHOLD = 0.93
    HR_THRESHOLD = 110

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

    def get_group_overview(self):
        sensors = ['ecg_sensor']
        data = {}
        response = self._db_handler.get(['group_data', self._group_id])
        if not response:
            print("ERROR: Group Not Found")
            return None

        data['group_info'] = response
        data['user_overviews'] = {}
        for mem in response['members']:
            user_data = User(mem, self._db_handler).get_user_overview(
                sensors,
                "-1"
            )
            data['user_overviews'][mem] = user_data
            if user_data['ecg_sensor']["max_HR"] > 110:
                data['at_risk_hr'] = {mem: user_data['ecg_sensor']}
            if user_data['ecg_sensor']["max_temp"] > 100.0:
                data['at_risk_temp'] = {mem: user_data['ecg_sensor']}
            if user_data['ecg_sensor']["min_ox"] < 0.93:
                data['at_risk_ox'] = {mem: user_data['ecg_sensor']}
            user_eval = User(
                mem,
                self._db_handler
            ).get_user_evaluations()
            data['user_evals'] = {mem: user_eval}
        return data
