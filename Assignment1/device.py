from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication

class Device:
    def __init__(self, sensor, data_processor, communication):
        self.sensor = sensor
        self.data_processor = data_processor
        self.communication = communication
        self.data = []


    def collect_data(self, num_samples):
        try:
            for _ in range(num_samples):
                my_Sensor = Sensor(0, 100)
                self.data.append(my_Sensor.read_data())
        except Exception as e:
            print(f"Error collecting data: {e}")

    def process_data(self):
        try:
            average = self.data_processor.calculate_average(self.data)
            min_value = self.data_processor.calculate_min(self.data)
            max_value = self.data_processor.calculate_max(self.data)
            return average, min_value, max_value
        except Exception as e:
            print(f"Error processing data: {e}")

    def send_data_to_server(self, processed_data):
        try:
            self.communication.send_data(processed_data)
        except Exception as e:
            print(f"Error sending data to server: {e}")

    def receive_data_from_server(self):
        try:
            self.communication.receive_data()
        except Exception as e:
            print(f"Error receiving data from server: {e}")
