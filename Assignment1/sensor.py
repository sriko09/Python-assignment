import random
from datetime import datetime
class Sensor:
    def __init__(self,mini,maxi):
        self.data = random.uniform(mini,maxi)
        self.timestamp = datetime.now().time()

    def read_data(self):
        format_time = self.timestamp.strftime("%H:%M:%S")
        return self.data, format_time


