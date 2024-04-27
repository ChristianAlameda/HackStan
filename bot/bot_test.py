from bot import Bot

def main():
    test_url, test_port = None, None
    newBot = Bot()
    newBot.connect(test_url, test_port)
    # while True:
    user_input = input('You: ')
    newBot.chat(user_input)

if __name__ == '__main__':
    main()