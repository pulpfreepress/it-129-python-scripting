# Client-Server Command Protocol Example

This example application builds upon the Simple Echo Server. It demonstrates how to send commands to the server from the client, process those commands on the server, encode data into JSON before returing to client, and decoding the JSON data on the client side.

## Server Listens on All Available Host IPs
Another change to this application, beside the addition of commands and JSON encoding & decoding, is the server listens on all available host IPs in addition to 127.0.0.1. 

## Default Port
The server listens on port 5500 by default. 

## To Run The Application

1. Launch a terminal window and start server. 
2. Launch another terminal window and start a client. Ensure it's connecting to the same `ip` address and `port`
3. Use client to send messages to server. See the messages appear on the server's terminal window. 
4. Launch more clients and send messages to server from multiple clients. 
5. To quit a client application type `quit`
6. To shutdown the server type `shutdown server`

