from bot import Bot

def main():
    test_url, test_port, test_cookie = '76.20.82.68', '39941', 'fdc851dc-ae95-412b-bfc6-711687b8058b'
    # http://76.20.82.68:39941/?cookie=153aae7b-27e3-4d7b-899c-de60893d077b&__theme=dark
    newBot = Bot()
    newBot.connect(test_url, test_port, test_cookie)
    # while True:
    user_input = input('You: ')
    print(newBot.chat(user_input))

if __name__ == '__main__':
    main()