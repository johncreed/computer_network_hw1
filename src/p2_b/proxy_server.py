from socket import *
import sys
import time
import threading
from http import HTTPStatus
import random as rd

if len(sys.argv) <= 2:
        print('Usage : "python ProxyServer.py server_ip server_port"\n[server_ip : It is the IP Address Of Proxy Server & Web server.')
        sys.exit(2)
server_ip=sys.argv[1]
server_port=int(sys.argv[2])

# Environment : Python 3.8
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Re-use the socket
# TODO in start.
port = rd.randint(1024, 9999)
print("Use port {}".format(port), flush=True)
tcpSerSock.bind(('', port))
tcpSerSock.listen(5)
# TODO in end.

def routine(tcpCliSock):
        # Strat receiving data from the client
        message = tcpCliSock.recv(1024).decode('utf-8')
        print(message)
        # Extract the filename from the given message
        print(message.split()[1])
        filename = message.split()[1].partition("/")[2]
        print(filename)
        filetouse = "/" + filename
        print(filetouse)
        try:
                # Check wether the file exist in the cache
                f = open(filetouse[1:], "r")
                print('Read from cache')
                outputdata = f.read()
                # ProxyServer finds a cache hit and generates a response message
                response_msg = b"HTTP/1.0 200 OK\r\n"
                response_msg += b"Content-Type:text/html\r\n\r\n"
                response_msg += outputdata.encode()
                tcpCliSock.send(response_msg)

        # Error handling for file not found in cache
        except IOError:
                # Create a socket on the proxyserver
                c = socket(AF_INET, SOCK_STREAM)
                try:
                        # Connect to the socket to port 80
                        c.connect((server_ip, server_port))
                        # ask port 127.0.0.1:80 for the file requested by the client
                        request = "GET /{} HTTP/1.1\n\n".format(filename)
                        c.send(request.encode())
                        # receive and check the response
                        # TODO in start.
                        server_response = c.recv(1024).decode('utf-8')
                        print("---- server_response ---")
                        print(server_response)
                        print("------------------------")
                        status_code = server_response.split()[1]
                        if(status_code == HTTPStatus.NOT_FOUND.value):
                            raise 
                        # TODO in end.

                        # Create a new file in the cache for the requested file.
                        # Also send the response in the buffer to client socket and the corresponding file in the cache
                        tmpFile = open(filename,"w")
                        entity_start = server_response.find('\n\n') + 2
                        html_content = server_response[entity_start:]
                        tmpFile.write(html_content)
                        tmpFile.close()

                        tmpFile = open(filename,"r")
                        outputdata = tmpFile.read()
                        response = 'HTTP/1.0 200 OK\r\n\r\n' + outputdata
                        tcpCliSock.send(response.encode())
                except:
                        print("Illegal request")
                        # HTTP response message for file not found
                        response = 'HTTP/1.0 404 Not Found\r\n\r\n'
                        tcpCliSock.send(response.encode())
                c.close()
        # Close the client and the server sockets. For testing multi-user, you should comment the tcpCliSock.close()
        tcpCliSock.close()

# TODO in start. Change this part, such that multi-users can connect to this proxy server
while True:
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)
        d = threading.Thread(name=str(addr), target=routine, args=(tcpCliSock,))
        d.setDaemon(True)
        d.start()
tcpSerSock.close()
# TODO in end.
