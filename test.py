
from douyu.chat.room import ChatRoom
from handler_message import msg_handler

def on_chat_message(msg):
    # with open("log.txt", "a") as f:
    #     f.write('[%s]:%s' % (msg.attr('nn'), msg.attr('txt')))
    print('[%s]:%s' % (msg.attr('nn'), msg.attr('txt')))
    msg_handler(msg.attr('txt'))



def run():
    room = ChatRoom('4655424')
    room.on('chatmsg', on_chat_message)
    room.knock()


if __name__ == '__main__':
    run()