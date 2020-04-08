#import socket module
from socket import *
import time
import sys # In order to terminate the program
import random as rd
import os.path

serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
port = rd.randint(1024, 9999)
print("Use port {}".format(port), flush=True)
serverSocket.bind(('', port))
serverSocket.listen(0)

while True:
    #Establish the connection
    print('Ready to serve...', flush=True)
    # TODO start

    connectionSocket, addr = serverSocket.accept()

    # TODO end
    try:
        # Receive http request from the clinet
        # TODO start

        message = connectionSocket.recv(1000)
        # TODO end
        print(message, flush=True)

        filename = message.split()[1].decode('utf-8')
        file_path = os.path.join('html', filename.strip('/'))
        print(file_path)
        f = open(file_path)

        # Read data from the file that the client requested
        # Split the data into lines for future transmission
        # TODO start

        outputdata = f.read()
        f.close()

        # TODO end
        print(outputdata, flush=True)

        #Send one HTTP header line into socket
        # TODO start

        # send HTTP status to client

        connectionSocket.send(b'HTTP/1.0 200 OK\r\n')

        # send content type to client

        connectionSocket.send(b'Content-Type: text/html\r\n\r\n')

        # TODO end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
    except IOError:
        print("File Not found", flush=True)
        #Send response message for file not found
        connectionSocket.send(b'HTTP/1.0 404 Not Found\r\n\r\n')

        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data

