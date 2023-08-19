import random
from datetime import datetime

# explain the code in comments
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

def main():
    sensor = Sensor(0, 100)
    #Creating a new Sensor from sensor class. Giving the range between 0 to 100 to generate random values
    #print (sensor)

    data_processor = DataProcessor()
    #Implementing a DataProcessor from data_processor class. The constructor just creates an empty list. The constructor doesn't take any parameters.

    communication = Communication("https://central-server.example.com")
    #Implementing a new communication type from communication class. The constructor takes an url as parameter and recieves and sends data to that.

    device = Device(sensor, data_processor, communication)
    #Implementing a Device type from device class that takes classes sensor, data_processor and communication as parameters in its Constructor. The constructor takes data from the three classes and also instantiates the instance data as an empty list.

    dashboard = Dashboard()
    #Implementing a new Dashboard type from dashboard class.

    device.collect_data(10)
    #The collect_data method from device class takes the number of samples needed as parameter and takes the values for the number of samples needed from sensor class and appends them to the list of data.

    processed_data = device.process_data()
    #processed_data = data_processor.calculate_average(device.data)
    #print(processed_data)

    print(device.process_data())
    #The method process_data from device class calculates the average, min and max of the data values, returns them and stores it in the variable processed_data
    #print ('Dolfi', processed_data)

    device.send_data_to_server(processed_data) 
    #This method uses the communication class to send the processed data to the server. The communication class takes an url as a parameter and sends the data to that

    device.receive_data_from_server()
    #This method uses the communication class to receive data from a given url

    print(device.data)

    dashboard.display_data(device.data)
    #This method takes the device.data which is randomly generated through sensor and plots a graph with it. The x-axis is the randomly generated data and the y-axis is the current timestamp.

    dashboard.display_analytics(processed_data)
    #This method takes the processed data which contains the average, minimum and maximum values of the data and graphs it. This method helps us get a better understanding of the data.

if __name__ == "__main__": # This checks if we are in the main program and only runs the code inside the if statement if it is run directly by the python interpreter. The code inside the if statement will not run if the file's code is imported via a module
    main()
