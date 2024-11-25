""" Main entry point for Simple Echo Server Client application.
Client attempts to connect to server on IP Address and Port. 
Default values are set to 127.0.0.1 (localhost) and 5500.
Server must be running and listening on that IP and Port before 
the client can connect. Client program runs until either user
enters 'quit' or 'shutdown server'.
"""
from client import Client

def main():
    ip_address = input('Server IP: ')
    c1 = Client(ip_address, 5500)
    message = ""
    while (message != 'quit') and (message != 'shutdown server'):
        message = input("Enter message to server: ")
        c1.send(message)

if __name__ == '__main__':
    main()