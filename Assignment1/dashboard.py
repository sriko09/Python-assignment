import random
import matplotlib.pyplot as plt
from datetime import datetime
from sensor import Sensor
from data_processor import DataProcessor

class Dashboard:
    def display_data(self, data):
        my_data, my_timestamp = zip(*data)
        x = list(my_data)
        y = list(my_timestamp)
        plt.plot(x,y)
        plt.xlabel("Data")
        plt.ylabel("TimeStamp")
        plt.title("Display data")
        plt.show


# compelet this function to display the data

    def display_analytics(self, analytics):
        data = {'Average': analytics[0], 'Minimum': analytics[1], 'Maximum': analytics[2]}
        my_data = list(data.keys())
        values = list(data.values())
        fig = plt.figure(figsize = (10, 5))
        plt.bar(my_data, values, color = 'maroon', width = 0.3)
        plt.title("The analytics of data")
        plt.show()



# complete this function to find the max, min , average of the red data

# Bonos!
# you can also generate some figures using the data and python modules like matplotlib, etc
# if simple GUI can be used. Hint: you can use django
# any extra flavor that you think it can add to the task. Hint(use your imagination and skills)
