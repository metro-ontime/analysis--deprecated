import json
from datetime import datetime

class MetroResponse:
    def __init__(self, json_from_metro):
        self.data = json_from_metro

    def parse(self):
        full_response = self.data.read()
        return json.loads(full_response)["items"]

    def timestamp(self):
        time_string = self.data.info()['Date']
        date_obj = datetime.strptime(time_string, '%a, %d %b %Y %H:%M:%S %Z')
        return date_obj.timestamp()
