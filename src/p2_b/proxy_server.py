from socket import *
import sys
import time
import threading
from http import HTTPStatus
from send_read_function import *

server_ip='127.0.0.1'
server_port=8888

# Environment : Python 3.8
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Re-use the socket
# TODO in start.
port = 8080
print("Use port {}".format(port), flush=True)
tcpSerSock.bind(('', port))
tcpSerSock.listen(5)
# TODO in end.

def process_request( tcpCliSock, request, headers, body):
    # Extract the filename from the given message
    filename = request['url'].strip('/')
    print(filename)
    try:
        # Check wether the file exist in the cache
        f = open(filename, "r")
        print('Read from cache')
        outputdata = f.read()

        # ProxyServer finds a cache hit and generates a response message
        response_msg = b'HTTP/1.0 200 OK\r\n'
        response_msg += b'Content-Type: text/html\r\n'
        response_msg += "Content-Length: {}\r\n".format(len(outputdata)).encode()
        response_msg += b'Connection: close \r\n'
        response_msg += b'\r\n'

        # Send the content of the requested file to the client
        response_msg += outputdata.encode()
        tcpCliSock.send(response_msg)

    # Error handling for file not found in cache
    except IOError:
        # Create a socket on the proxyserver
        c = socket(AF_INET, SOCK_STREAM)
        try:
            # Ask port 127.0.0.1:80 for the file requested by the client
            c.connect((server_ip, server_port))
            request_msg = "GET {} HTTP/1.1\r\n".format(request['url']).encode()
            request_msg += b'Content-Type: text/html\r\n'
            request_msg += b'\r\n'
            c.send(request_msg)

            # receive and check the response
            respond, headers, body = respond_read( c )
            print("---- Web Server Response ---")
            print(respond, headers, body)
            print("----------------------------")
            if(respond['code'] == HTTPStatus.NOT_FOUND.value):
                raise IOError

            # Create a new file in the cache for the requested file.
            # Also send the response in the buffer to client socket and the corresponding file in the cache
            tmpFile = open(filename,"w")
            tmpFile.write(body)
            tmpFile.close()

            tmpFile = open(filename,"r")
            outputdata = tmpFile.read()
            #Send one HTTP header line into socket
            response_msg = b'HTTP/1.0 200 OK\r\n'
            response_msg += b'Content-Type: text/html\r\n'
            response_msg += "Content-Length: {}\r\n".format(len(outputdata)).encode()
            response_msg += b'Connection: close \r\n'
            response_msg += b'\r\n'

            # Send the content of the requested file to the client
            response_msg += outputdata.encode()
            tcpCliSock.send(response_msg)
        except IOError:
            print("Illegal request")
            # HTTP response message for file not found
            response_msg = b'HTTP/1.0 404 Not Found\r\n'
            response_msg += b'Content-Type: text/html\r\n'
            response_msg += "Content-Length: {}\r\n".format(len(body)).encode()
            response_msg += b'Connection: close \r\n'
            response_msg += b'\r\n'

            # Send the content of the requested file to the client
            response_msg += body.encode()
            tcpCliSock.send(response_msg)
            print(body)
        c.close()

def routine(tcpCliSock):
    # Strat receiving data from the client
    try:
        request, headers, body = request_read( tcpCliSock )
        print("------ client_request ---")
        print(request, headers, body)
        print("------------------------")
        process_request(tcpCliSock, request, headers, body)
    except  IOError:
        print("Connection closed")

    tcpCliSock.close()

while True:
    print('Proxy ready to serve...')
    tcpCliSock, addr = tcpSerSock.accept()
    print('Received a connection from:', addr)
    d = threading.Thread(name=str(addr), target=routine, args=(tcpCliSock,))
    d.setDaemon(True)
    d.start()
tcpSerSock.close()
