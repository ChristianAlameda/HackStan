import tensorflow as tf

class Bot():
    def __init__(self):
        self.__chatbot = None

    def __del__(self):
        del self.__chatbot

    def train(self, dataset=None):
        conversation = [
            "Hello",
            "Hi there!",
            "How are you doing?",
            "I'm doing great.",
            "That is good to hear",
            "Thank you.",
            "You're welcome."
        ]

        trainer = None

        trainer.train(conversation)
        print('Training completed.')
        return True

    def chat(self, input):
        response = self.__chatbot.get_response(input)
        print(response)
        return response
# end Bot