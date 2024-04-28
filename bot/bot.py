import bot.rtx_api_3_5 as rtx_api
import string
from threading import Thread

class Bot():
    def __init__(self):
        self.__url = None
        self.__port = None
        self.__cookie = None
        self.__history = []
        self.__threads = []

    def __del__(self):
        del self.__url, self.__port, self.__history

    def chat(self, userInput):
        self.__threads.append(Thread(target=self.__history.append, name='input', args=[str(userInput)]))
        self.__threads[-1].start()
        response = rtx_api.send_message(userInput)
        # We need to remove everything after, and including, <br>Reference files:<br>
        word = ''
        wordStart = 0
        
        for i, c in enumerate(response):
            if word == 'br' and response[wordStart-1] == '<':
                break
            elif c == ' ' or c in string.punctuation:
                word = ''
                wordStart = i+1
            else:
                word += c
        response = response[:wordStart-1]
        if self.__threads[-1].is_alive():
            self.__threads[-1].join()
        self.__threads.pop()
        self.__history.append(str(response))
        return response
    
    # def connect(self, test_url, test_port, test_cookie):
    #     if rtx_api.connect(test_url, test_port,test_cookie):
    #         self.__url = test_url
    #         self.__port = test_port
    #         self.__cookie = test_cookie

    def getHistory(self):
        return self.__history
# end Bot
