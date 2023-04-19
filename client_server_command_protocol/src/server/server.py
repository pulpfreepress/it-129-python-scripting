""" Implements a multithreaded server that echos messages received from
connected clients. 
"""

import socket
import threading
import sys
import platform
import os
import random
import json


class Server():
    """ Implements the Server class.
    """
 
    

    def __init__(self, ip, port):
        """ Constructor method. Takes two arguments: ip address and port.
        The ip address is a string in the form of an IPv4 address. 
        (Example: "127.0.0.1") The port is an integer representing an 
         operating system port on which the server application listens for
         incomming connections. (Example: 5500) The port used must not already be
         used by another application.
        """
        self._motivational_message_list = []
        self._initialize_motivational_message_list()
        self.ip = ip
        self.port = port
        self._listen(ip, port)
        self._accept_connection()
        
       

    # Listen for incoming connections
    def _listen(self, ip, port):
        """ Creates a server socket and starts listening on assigned 
        IP Address and Port.
        """
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if os.name == 'nt':
                self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            else:
                self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            self.server.bind((ip, port))
            print(f'Listening on IP Address: {ip} and Port: {port} ')
            self.server.listen(4)
        except Exception as e:
            print(f'Problem listening for incoming connection: {e}')
            self.server.close()
            sys.exit(0)

    # Accept incoming connection
    def _accept_connection(self):
        """ Accepts incoming client connections and hands off request processing
        to new thread.
        """
        try:
            with self.server:
                while True:
                    print(f'Waiting for incoming client connection...')
                    client, address = self.server.accept()
                    print(f'Accepted client connection from IP Address: {address[0]} and {address[1]}')
                    client_handler = threading.Thread(target=self._process_client_requests, args=(client, self.server, self._motivational_message_list))
                    client_handler.start()
        except Exception as e:
            print(f'Problem accepting connection: {e}')

    # Process connection in separate thread
    def _process_client_requests(self, client, server, message_list):
        """ Processes communication between client and server. 
        """
        try:
            with client:
                while True:
                    raw_request = client.recv(1024)
                    if not raw_request:
                        break
                    request = raw_request.decode('utf-8')
                    print(f'request from client: {request}')

                    match(request):
                        case 'shutdown server':
                            server.close()
                            break

                        case 'random':
                            response = self._random()
                            client.send(bytearray(response, 'utf-8'))

                        case 'sysinfo':
                            response = self._sys_info()
                            client.send(bytearray(response, 'utf-8'))

                        case 'motivation':
                            response = self._motivation(message_list)
                            client.send(bytearray(response, 'utf-8'))
                            
                        case _: 
                            response = self._echo(request)
                            client.send(bytearray(response, 'utf-8'))
                            

        except Exception as e:
            print(f'Problem processing client requests: {e}')


    def _initialize_motivational_message_list(self):
        self._motivational_message_list.append('You\'re doing great!')
        self._motivational_message_list.append('Keep up the amazing work!')
        self._motivational_message_list.append('You are A-W-E-S-O-M-E!')
        self._motivational_message_list.append('Let nothing stand in your way!')
        self._motivational_message_list.append('Today you may struggle but tomorrow you will SUCCEED!')
        self._motivational_message_list.append('You look marvelous!')

    def _random(self):
        dictionary = {} # Define a dictionary
        dictionary['command'] = 'random' # Key to store the executed command
        dictionary['results'] = random.randint(0, 1000) # Uses the random library
        return json.dumps(dictionary)
    
    def _sys_info(self):
        dictionary = {} # Create a dictionary
        dictionary['command'] = 'sysinfo'
        dictionary['results'] = {} # Create another dictionary to hold complex results
        dictionary['results']['machine'] = platform.machine() # Uses the platform library 
        dictionary['results']['node'] = platform.node()
        dictionary['results']['platform'] = platform.platform()
        dictionary['results']['processor'] = platform.processor()
        dictionary['results']['pythonVersion'] = platform.python_version()
        return json.dumps(dictionary)
    
    def _motivation(self, message_list):
        max_list_index = len(message_list) - 1
        random_index = random.randint(0, max_list_index)
        dictionary = {}
        dictionary['command'] = 'motivation'
        dictionary['results'] = message_list[random_index]
        return json.dumps(dictionary)
    
    def _echo(self, message):
        dictionary = {} # Create a dictionary
        dictionary['command'] = 'default echo' # Add a key to store the command just executed
        dictionary['results'] = message # Add a key to store the results
        return json.dumps(dictionary) # Convert the dictionary into a JSON string with json.dumps() method
