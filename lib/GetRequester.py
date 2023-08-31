import requests
import json

class GetRequester:

    # object is initialized with url on creation
    #From Lab:
    #Start by creating a GetRequester class. This class should be able to initialize 
    #with a string URL.

    def __init__(self, url):
        self.url = url

    # Method used to send a get request to url and a receive a response from url
    #From Lab:
    #the GetRequester class should have a get_response_body method that sends a GET 
    #request to the URL passed in on initialization. This method should return the 
    #body of the response.

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content
    
    #Method used to present the data in the way we need to it for our app
    #From Lab:
    #The GetRequester class should have a load_json method that should use 
    #get_response_body to send a request, then return a Python list or dictionary
    #made up of data converted from the response of that request.
    
    def load_json(self):
        data_list = []
        data = json.loads(self.get_response_body())
        for data in data:
            data_list.append(data)
        return data_list  

