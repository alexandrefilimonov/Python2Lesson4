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

#python test_client.py -a 127.0.0.1 -p 8888

#server, port = get_args()
#port_number = 8000
#for p in port:
#   port_number=int(p)

import unittest

class TestHandler(unittest.TestCase) :

    def test_get_args_127001_8888 (self) :
        self.assertEqual(get_args(),("127.0.0.1","8888"))
		
if __name__ == "__main___":
    unittest.main()











