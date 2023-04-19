# Client-Server Command Protocol Example

This example application builds upon the Simple Echo Server. It demonstrates how to send commands to the server from the client, process those commands on the server, encode data into JSON before returing to client, and decoding the JSON data on the client side.

## Server Listens on All Available Host IPs
Another change to this application, beside the addition of commands and JSON encoding & decoding, is the server listens on all available host IPs in addition to 127.0.0.1. 

## Default Port
The server listens on port 5500 by default. 

## To Run The Application

The application still functions as a simple echo server. If you send a message to the server it does not recognize as a command, it will simply return the message to the client. 

1. Launch a terminal window and start server. 
2. Launch another terminal window and start a client. Ensure it's connecting to the same `ip` address and `port`
3. Use client to send messages to server. See the messages appear on the server's terminal window. 
4. Launch more clients and send messages to server from multiple clients. 
5. To quit a client application type `quit`
6. To shutdown the server type `shutdown server`

Note that `shutdown server` is a command, but it does not return any data to the client. It simply shuts down the server application no questions asked.

# Example Commands

Besides `shutdown server`, this example implements the following additional commands:

| Command | Description |
|---------|--------------|
| `random` | Requests a random number from the server |
| `sysinfo` | Requests information about the server |
| `motivation` | Requests a pithy motivational statement from the server |

I just dreamed up these commands while waiting for my car to be serviced. 

# What YOU Need To Do

You need to implement at least 3 additional commands.

- Study this example and see how I have implemented each command
- Think up some commands of your own and implement them in similar fashion, but don't let what I did limit your creativity.
- Study the following libraries for ideas of what you can do on the server side:
  - os
  - platform
  - requests

