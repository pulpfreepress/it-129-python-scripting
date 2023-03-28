import socket
import threading
import sys


class Server():
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self._listen(ip, port)
        self._accept_connection()

    # Listen for incoming connections
    def _listen(self, ip, port):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
            self.server.bind((ip, port))
            print(f'Listening on IP Address: {ip} and Port: {port} ')
            self.server.listen(4)
        except Exception as e:
            print(f'Problem listening for incomming connection: {e}')
            self.server.close()
            sys.exit(0)

    # Accept incoming connection
    def _accept_connection(self):
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