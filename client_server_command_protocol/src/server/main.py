""" Main entry point for Server application.
Default values are set to: IP Address 127.0.0.1 (localhost)
and Port 5500. 
"""
from server import Server

def main():
    s1 = Server("127.0.0.1", 5500)


if __name__ == "__main__":
    main()
