from client import Client

def main():
    c1 = Client("127.0.0.1", 5500)
    message = ""
    while (message != 'quit') and (message != 'shutdown server'):
        message = input("Enter message to server: ")
        c1.send(message)

if __name__ == '__main__':
    main()