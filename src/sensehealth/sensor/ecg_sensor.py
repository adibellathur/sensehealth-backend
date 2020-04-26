"""ECG Sensor Handler."""
import os
import time
import random
import numpy as np
from .sensor import Sensor
from twilio.rest import Client

def send_sms(self):
    # account_sid = os.environ['TWILIO_ACCOUNT_SID']
    # auth_token = os.environ['TWILIO_AUTH_TOKEN']
    # _to = os.environ['TO_NUMBER']
    # _from = os.environ['FROM_NUMBER']
    #
    # client = Client(account_sid, auth_token)
    #
    # message = client.messages.create(
    #      body="You may have been exposed to COVID-19, \
    #      please follow your Health Protocol immediately",
    #      from_=_from,
    #      to=_to
    #  )
     return


class ECGSensor(Sensor):
    """Class to handle ECG sensor data."""

    def __init__(self, user_id, db_handler):
        """Construct object."""
        super().__init__(user_id, db_handler)
        return

    def parse_data(self, data, timestamp, send_to_db=True):
        """Parse JSON for relevant data."""
        # TODO: parse the data to include only useful things
        print(data)
        parsed = {}
        parsed["HR"] = sum(data["HR"]) / len(data["HR"])
        parsed["PatchId"] = data["PatchId"]
        if "ECG LEAD A" in data:
            parsed["ECG_CH_A"] = data["ECG LEAD A"]
            parsed["ECG_CH_B"] = data["ECG LEAD B"]
        if "ECG_CH_A" in data:
            parsed["ECG_CH_A"] = data["ECG_CH_A"]
            parsed["ECG_CH_B"] = data["ECG_CH_B"]
        parsed["LeadStatus"] = data["LeadStatus"]
        parsed["temp"] = random.uniform(96.0, 101.0)
        parsed["pulse_oximeter"] = random.uniform(0.93, 0.99)

        if parsed["HR"] > 120 or parsed["HR"] < 60:
            send_sms()
        elif parsed["temp"] > 101 or parsed["pulse_oximeter"] < .9:
            send_sms()

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

    def get_data_overview(self, start_time):
        """Summarize data from database."""
        overview = {}
        hrs = []
        oxs = []
        temps = []
        data = self.fetch_data(start_time)
        for key in data:
            if (type(data[key]) is dict) and\
                    "HR" in data[key] and\
                    data[key]["HR"] != -1:
                hrs.append(data[key]["HR"])
            oxs.append(data[key]["pulse_oximeter"])
            temps.append(data[key]["temp"])
        hrs = np.array(hrs)
        oxs = np.array(oxs)
        temps = np.array(temps)
        overview['max_temp'] = np.amax(temps)
        overview['av_temp'] = np.average(temps)
        overview['min_ox'] = np.amin(oxs)
        overview['av_ox'] = np.average(oxs)
        overview['max_HR'] = np.amax(hrs)
        overview['av_HR'] = np.average(hrs)
        return overview
