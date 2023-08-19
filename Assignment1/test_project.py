import unittest
from sensor import Sensor
from device import Device
from data_processor import DataProcessor
from communication import Communication

class Testcases(unittest.TestCase):

    #Test Sensor
    def test_read_data(self):
        my_Sensor = Sensor(0, 100)
        self.mylist = []
        self.mylist.append(my_Sensor.read_data())
        assert len(self.mylist) == 1
        assert (self.mylist[0][0]) <= 100
        assert (self.mylist[0][0]) >= 0

    #Test device
    def test_collect_data(self):
        with self.assertRaises(Exception):
            sensor = Sensor(0,100)
            self.device = Device(sensor,data_processor = DataProcessor(),communication = Communication("url"))
            self.device.collect_data(-1)

    def test_process_data(self):

        with self.assertRaises(Exception):
            self.device.process_data()

    def test_send_data_to_server(self):
        with self.assertRaises(Exception):
            self.device.send_data_to_server(self.device.process_data())

    def test_receive_data_from_server(self):
        with self.assertRaises(Exception):
            self.device.receive_data_from_server()

    #Test data_processor
    def test_calculate_min(self):
        self.list1 = [(76.58883279715093, '14:43:18'), (47.6447597497028, '14:43:18'), (92.37234097709036, '14:43:18'), (59.15366812780658, '14:43:18'), (87.60491243443228, '14:43:18'), (4.974302619748894, '14:43:18'), (31.00793124116915, '14:43:18'), (3.286060461227591, '14:43:18'), (19.83486960771731, '14:43:18'), (78.50706603481152, '14:43:18')]
        assert DataProcessor.calculate_min(self.list1) == 3.286060461227591

    def test_calculate_max(self):
        self.list1 = [(76.58883279715093, '14:43:18'), (47.6447597497028, '14:43:18'), (92.37234097709036, '14:43:18'), (59.15366812780658, '14:43:18'), (87.60491243443228, '14:43:18'), (4.974302619748894, '14:43:18'), (31.00793124116915, '14:43:18'), (3.286060461227591, '14:43:18'), (19.83486960771731, '14:43:18'), (78.50706603481152, '14:43:18')]
        assert DataProcessor.calculate_max(self.list1) == 92.37234097709036

    def test_calculate_average(self):
        self.list1 = [(76.58883279715093, '14:43:18'), (47.6447597497028, '14:43:18'), (92.37234097709036, '14:43:18'), (59.15366812780658, '14:43:18'), (87.60491243443228, '14:43:18'), (4.974302619748894, '14:43:18'), (31.00793124116915, '14:43:18'), (3.286060461227591, '14:43:18'), (19.83486960771731, '14:43:18'), (78.50706603481152, '14:43:18')]
        assert DataProcessor.calculate_max(self.list1) == 50.097474405085734

    
