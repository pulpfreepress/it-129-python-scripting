""" Implements a multithreaded server that echos messages received from
connected clients. 
"""

import socket
import threading
import sys
import os


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
                    print(f'Waiting for incoming commection...')
                    client, address = self.server.accept()
                    print(f'Accepted client connection from IP Address: {address[0]} and {address[1]}')
                    client_handler = threading.Thread(target=self._process_client_requests, args=(client, self.server))
                    client_handler.start()
        except Exception as e:
            print(f'Problem accepting connection: {e}')

    # Process connection in separate thread
    def _process_client_requests(self, client, server):
        """ Processes communication between client and server. 
        """
        try:
            with client:
                while True:
                    request = client.recv(1024)
                    if not request:
                        break
                    message = request.decode('utf-8')
                    print(f'Message from client: {message}')
                    match(message):
                        case 'shutdown server':
                            server.close()

                    response = message
                    client.send(bytearray(response, 'utf-8'))

        except Exception as e:
            print(f'Problem processing client requests: {e}')