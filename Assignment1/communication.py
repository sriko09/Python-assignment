# comment each line with an explination, at the end  the code should be veiwed as it is written by you (a professional developer)

class Communication: #Creating a class named communication
    def __init__(self, server_url): #Creating a constructor that takes a parameter and the value of that it is stored in server_url
        self.server_url = server_url #self.server_url creates an instance of this class and it is taking the value of server_url that was passed as parameter through the function. 

    def send_data(self, data): #This method takes data as a parameter
        print(f"Sending data to {self.server_url}: {data}") #This method takes the data passed through the parameter and sends it to the url that was passed through the constructor. 

    def receive_data(self): #This method is created to recieve data from the url
        print(f"Receiving data from {self.server_url}") #Recieves data from the url and prints that it recieved data from the url. 
