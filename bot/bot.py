import rtx_api_3_5 as rtx_api
from threading import Thread

class Bot():
    def __init__(self):
        self.__url = None
        self.__port = None
        self.__history = []
        self.__threads = []

    def __del__(self):
        del self.__url, self.__port, self.__history

    def chat(self, userInput):
        self.__threads.append(Thread(target=self.__history.append, name='input', args=userInput))
        self.__threads[-1].start()
        if not self.__url:
            print('No connection. Please connect to the server first.')
            return 'No connection.' 
        response = rtx_api.send_message_public(userInput, self.__url, self.__port)
        if self.__threads[-1].is_alive():
            self.__threads[-1].join()
        self.__threads.pop()
        self.__history.append(response)
        return response
    
    def connect(self, test_url, test_port):
        if rtx_api.connect(test_url, test_port):
            self.__url = test_url
            self.__port = test_port

    def getHistory(self):
        return self.__history
# end Bot