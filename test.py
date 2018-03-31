
from douyu.chat.room import ChatRoom


def on_chat_message(msg):
    # with open("log.txt", "a") as f:
    #     f.write('[%s]:%s' % (msg.attr('nn'), msg.attr('txt')))
    print('[%s]:%s' % (msg.attr('nn'), msg.attr('txt')))


def run():
    room = ChatRoom('633019')
    room.on('chatmsg', on_chat_message)
    room.knock()


if __name__ == '__main__':
    run()