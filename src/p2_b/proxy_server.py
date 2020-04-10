from socket import *
import sys
import time
import threading

if len(sys.argv) <= 2:
        print('Usage : "python ProxyServer.py server_ip server_port"\n[server_ip : It is the IP Address Of Proxy Server & Web server.')
        sys.exit(2)
server_ip=sys.argv[1]
server_port=int(sys.argv[2])

# Environment : Python 3.8
# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# Fill in start.
tcpSerSock.bind(('', 8080))
tcpSerSock.listen(5)
# Fill in end.
def routine(tcpCliSock):
        # Strat receiving data from the client
        message = tcpCliSock.recv(1024).decode('utf-8')
        print(message)
        # Extract the filename from the given message
        print(message.split()[1])
        filename = message.split()[1].partition("/")[2]
        print(filename)
        fileExist = "false"
        filetouse = "/" + filename
        print(filetouse)
        try:
                # Check wether the file exist in the cache
                f = open(filetouse[1:], "r")
                outputdata = f.read()
                fileExist = "true"
                # ProxyServer finds a cache hit and generates a response message
                tcpCliSock.send("HTTP/1.0 200 OK\r\n\r\n".encode())
                tcpCliSock.send("Content-Type:text/html\r\n\r\n".encode())
                # Fill in start.

                # Fill in end.
                print('Read from cache')
        # Error handling for file not found in cache
        except IOError:
                if fileExist == "false":
                        # Create a socket on the proxyserver
                        c = socket(AF_INET, SOCK_STREAM)
                        try:
                                # Connect to the socket to port 80
                                c.connect((sys.argv[1],80))
                                # ask port 127.0.0.1:80 for the file requested by the client
                                request = "GET " + "/" + filename + " HTTP/1.1\n\n"
                                c.send(request.encode())
                                # receive the response 
                                # Fill in start.

                                # Fill in end.
                                # Create a new file in the cache for the requested file.
                                # Also send the response in the buffer to client socket and the corresponding file in the cache
                                tmpFile = open("./" + filename,"w")
                                # Fill in start.
                                html_content = 
                                # Fill in end.

                                tmpFile.write(html_content)
                                tmpFile.close()
                                tmpFile = open("./" + filename,"r")
                                outputdata = tmpFile.read()
                                response = 'HTTP/1.0 200 OK\r\n\r\n' + outputdata
                                tcpCliSock.send(response.encode())
                                
                        except:
                                print("Illegal request")
                        c.close()
                else:
                        # HTTP response message for file not found
                        # Fill in start.

                        # Fill in end.
        # Close the client and the server sockets. For testing multi-user, you should comment the tcpCliSock.close()
        tcpCliSock.close()

# Fill in start. Change this part, such that multi-users can connect to this proxy server
while True:
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)
        routine(tcpCliSock)
tcpSerSock.close()
# Fill in end.
