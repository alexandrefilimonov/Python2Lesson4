#1)клиент отправляет запрос серверу;
#Функции клиента: 
#  +сформировать presence-сообщение; 
#  +отправить сообщение серверу; 
#  +получить ответ сервера; 
#  +разобрать сообщение сервера; 
#  +параметры командной строки скрипта client.py <addr> [<port>]: addr — ip-адрес сервера; 
#    port — tcp-порт на сервере, по умолчанию 7777. 
#python _alexfilimonov_client.py -a 127.0.0.1 -p 8888
import json 
from typing import Any, Dict 
from socket import *

import argparse

def get_args():
    # Assign description to the help doc
    parser = argparse.ArgumentParser(
        description='Script retrieves schedules from a given server')
    # Add arguments
    parser.add_argument(
        '-a', '--server', type=str, help='Server name', required=True)
    parser.add_argument(
        '-p', '--port', type=str, help='Port number', required=True, nargs='+')
    #parser.add_argument(
    #    '-k', '--keyword', type=str, help='Keyword search', required=False, default=None)
    # Array for all arguments passed to script
    args = parser.parse_args()
    # Assign args to variables
    server = args.server
    port = args.port[0].split(",")
    ##keyword = args.keyword
    # Return all variable values
    return server, port 

server, port = get_args()
port_number = 8000
for p in port:
   port_number=int(p)

while True :
    s = socket(AF_INET, SOCK_STREAM) 
    s.connect(( 'localhost' , port_number )) 
    msg = {"action" : "authenticate", "user" : {"account_name" : "alex", "password" : "alex_pwd"}}
    msg_str = json.dumps(msg)
    s.send(msg_str.encode( 'utf-8' ))
    data = s.recv( 1000000 )
    print( 'The message from server: ' , data.decode( 'utf-8' ), ', length ' , len(data), 'bytes' )
    s.close()

    s = socket(AF_INET, SOCK_STREAM) 
    s.connect(( 'localhost' , port_number )) 
    msg = {"action" : "msg", "to" : "room #1", "from" : "alex_account", "message" : "Hello, server!"}
    msg_str = json.dumps(msg)
    s.send(msg_str.encode( 'utf-8' ))
    data = s.recv( 1000000 )
    print( 'The message from server: ' , data.decode( 'utf-8' ), ', length ' , len(data), 'bytes' )
    s.close()
    
    s = socket(AF_INET, SOCK_STREAM) 
    s.connect(( 'localhost' , port_number )) 
    msg = {"action": "quit"}
    msg_str = json.dumps(msg)
    s.send(msg_str.encode( 'utf-8' ))
    data3 = s.recv( 1000000 )
    print( 'The message from server: ' , data3.decode( 'utf-8' ), ', length ' , len(data3), 'bytes' )
    s.close()
	
    break

