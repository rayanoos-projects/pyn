#!/usr/bin/env python
# -*- coding: utf-8 -*-
from sys import path
path.append('..')
from client import Client

bot_token = 'ppNOvEMAVMZI7pqYgetB5DYg8cgVZC1hy6PlO6n5ByMTK4DzlWIS67B2BOeCGQntnbOWFDO362Sm3QBLEzohD0NSXCPSwqR_R96HeG0_WDl09meG1WCppCoJd_EuQoKRzgbFkttrmTRokuaF'
def send(user , text):
    try:
        to = user

        [error, success] = bot.send_text(to, text)

        if success:
            print('Message sent successfully')
        else:
            print('Sending message failed: {}' .format(error))

    except Exception as e:
        print(e.args[0])

bot = Client(bot_token)

try:
    messages = bot.get_messages()
    for message in messages:
        print("New message from {} \nType: {}\nBody: {}" .format(message['from'], message['type'], message['body']))
        if message['type']=='START':
            send(message['from'],'هرچه مي خواهد دل تنگت بگو')
        elif message['body']=='سلام':
            send(message['from'],'سلام رايانوسم')
        else:
            send(message['from'],message['body'])

except Exception as e:
    print(e.args[0])
