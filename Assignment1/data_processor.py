import statistics
from sensor import Sensor

class DataProcessor:

    def calculate_min(self, data):
        my_data, my_timestamp = zip(*data)
        return min(my_data)


    def calculate_average(self, data):
        if len(data) == 0:
            return 0
        else:
            my_data, my_timestamp = zip(*data)
            avg = sum(my_data) / len(my_data)
            return avg


    def calculate_max(self, data):
        my_data, my_timestamp = zip(*data)
        return max(my_data)