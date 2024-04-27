import rtx_api_3_5 as rtx_api

class Bot():
    def __init__(self):
        self.__chatbot = None
        self.__url = None
        self.__port = None

    def __del__(self):
        del self.__chatbot

    def chat(self, userInput):
        response = rtx_api.send_message_public(userInput, self.__url, self.__port)
        return response
    
    def connect(self, test_url, test_port):
        if rtx_api.connect(test_url, test_port):
            self.__url = test_url
            self.__port = test_port
# end Bot