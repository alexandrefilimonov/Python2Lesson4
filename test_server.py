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
import unittest


def handle_authenticate(request) :
    if request['user']=={'account_name':'alex','password':'alex_pwd'}:
        return {"response": 200, "alert": "User alex authorized and authenticated successfully!"}
    else:
        return {"response": 402, "alert": "Error of authentication!"}

def handle_message(request) :
    return {"response": 200, "message": request['message']}

def handle_quit(request) :
    return {"response": 200, "action": "quit"}

def handler(request: Dict[str, object]) :
    print(f'Client sent {request}')
    response=mapping[request['action']] (request)
    print(f'Response {response}')
    return response 


class TestHandler(unittest.TestCase) :

    def test_handle_authenticate(self) :
        request['user']={'account_name':'alex','password':'alex_pwd'} 
        self.assertEqual(handle_authenticate(request),{"response": 200, "alert": "User alex authorized and authenticated successfully!"})

    def test_handle_message(self) :
        self.assertEqual(handle_message(request),{"response": 200, "message": request['message']})

    def test_handle_quit(self) :
        self.assertEqual(handle_quit(request), {"response": 200, "action": "quit"})  		
		
if __name__ == "__main___":
    unittest.main()
