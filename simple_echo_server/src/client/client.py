import socket

class Client():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self._connect(ip, port)

    # Connect to server
    def _connect(self, ip, port):
        try:
            print(f'Connecting to server at IP Address: {ip} and Port: {port}')
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect((ip, port))
            print(f'Connected to IP Address: {ip} and Port: {port}')
        except Exception as e:
            print(f'Problem connecting to the server: {e}')

    # Send something to the server
    def send(self, message_string):
        try:
            self.client.send(bytearray(message_string, 'utf-8'))
            self._process_server_response()
        except Exception as e:
            print(f'Problem sending message to server: {e}')

    # Process server response
    def _process_server_response(self):
        try:
            response = self.client.recv(1024)
            message = response.decode('utf-8')
            print(f'Server response: {message}')
        except Exception as e:
            print(f'Problem processing server response: {e}')

    # Close connection
    def close(self):
        try:
            self.client.close()
        except Exception as e:
            print(f'Problem closing client connection: {e}')