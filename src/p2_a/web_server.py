#import socket module
from socket import *
import time
import sys # In order to terminate the program
import os.path
from send_read_function import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
#Prepare a sever socket
port = 8888
print("Use port {}".format(port), flush=True)
serverSocket.bind(('127.0.0.1', port))
serverSocket.listen(0)

while True:
    #Establish the connection
    print('Ready to serve...', flush=True)
    connectionSocket, addr = serverSocket.accept()
    print("Connected by {}".format(addr))

    try:
        # Receive http request from the clinet
        request, headers, body = request_read( connectionSocket )

        filename = request['url'].strip('/')
        print(filename)
        f = open(filename)

        # Read data from the file that the client requested
        # Split the data into lines for future transmission
        outputdata = f.read()
        f.close()
        #print(outputdata, flush=True)

        #Send one HTTP header line into socket
        response_msg = b'HTTP/1.0 200 OK\r\n'
        response_msg += b'Content-Type: text/html\r\n'
        response_msg += "Content-Length: {}\r\n".format(len(outputdata)).encode()
        response_msg += b'Connection: close \r\n'
        response_msg += b'\r\n'

        # Send the content of the requested file to the client
        response_msg += outputdata.encode()
        connectionSocket.send(response_msg)

        #Close client socket
        connectionSocket.close()

    except (IOError, ValueError):
        print("File Not found", flush=True)
        f = open('404.html')
        outputdata = f.read()
        f.close()
        print(outputdata, flush=True)

        #Send response message for file not found
        response_msg = b'HTTP/1.0 404 Not Found\r\n'
        response_msg += b'Content-Type: text/html\r\n'
        response_msg += "Content-Length: {}\r\n".format(len(outputdata)).encode()
        response_msg += b'Connection: close \r\n'
        response_msg += b'\r\n'

        # Send the content of the requested file to the client
        response_msg += outputdata.encode()
        connectionSocket.send(response_msg)

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data

