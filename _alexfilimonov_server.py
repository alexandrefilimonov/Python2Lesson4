#2)сервер отвечает соответствующим кодом результата. 
#Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции. 
#+Функции сервера: 
#  +принимает сообщение клиента; 
#  +формирует ответ клиенту; 
#  +отправляет ответ клиенту; 
#  +имеет параметры командной строки: -p <port> — TCP-порт для работы (по умолчанию использует 7777); 
#    -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
#python _alexfilimonov_server.py -a 127.0.0.1 -p 8888

from socket import *
import time
import json 
from typing import Any, Dict 

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
   
#class Response:
#    def: __init__(self, status_code:int)
#        self.status_code = status_code
#    def: to_json(self)-> str 
#         return json.dumps({'response':self_status_code})
		
		
def handle_authenticate(request) :
    if request['user']=={'account_name':'alex','password':'alex_pwd'}:
        return {"response": 200, "alert": "User alex authorized and authenticated successfully!"}
    else:
        return {"response": 402, "alert": "Error of authentication!"}

def handle_message(request) :
    return {"response": 200, "message": request['message']}

def handle_quit(request) :
    return {"response": 200, "action": "quit"}
		
mapping = {
    'authenticate': handle_authenticate, 
    'msg': handle_message, 
    'quit': handle_quit
}

def handler(request: Dict[str, object]) :
    print(f'Client sent {request}')
    response=mapping[request['action']] (request)
    print(f'Response {response}')
    return response 

s = socket(AF_INET, SOCK_STREAM) # Создает сокет TCP
s.bind(( '' , port_number )) # Присваивает порт 8888
# одновременно обслуживает не более 5 запросов.
while True :
    s.listen( 5 ) # Переходит в режим ожидания запросов;
    client, addr = s.accept()
    with client: 
        data_b = client.recv( 1000000 )
        data = json.loads(data_b, encoding='utf-8')
        response = handler(data) 
        client.send(json.dumps(response).encode( 'utf-8' ))		
        #client.send(msg.encode( 'utf-8' ))
        if (data['action']=='quit') :
            client.close()
            break