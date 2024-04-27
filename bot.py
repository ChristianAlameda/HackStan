import tensorflow as tf
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

class Bot():
    def __init__(self):
        self.__chatbot = ChatBot("Titus")

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

        trainer = ListTrainer(self.__chatbot)

        trainer.train(conversation)
        print('Training completed.')
        return True

    def chat(self, input):
        response = self.__chatbot.get_response(input)
        print(response)
        return response
# end Bot