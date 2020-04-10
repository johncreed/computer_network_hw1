from socket import *
import sys
import random as rd
import os.path


if len(sys.argv) <= 1:
        print('Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server')
        sys.exit(2)

# Create a server socket, bind it to a port and start listening
tcpSerSock = socket(AF_INET, SOCK_STREAM)
# TODO start.

port = rd.randint(1024, 9999)
print("Use port {}".format(port), flush=True)
tcpSerSock.bind(('', port))
tcpSerSock.listen(0)

# TODO end.
while 1:
        # Strat receiving data from the client
        print('Ready to serve...')
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:', addr)

        # Receive request from the client
        # TODO start.
        message = tcpSerSock.recv(1000)
        # TODO end.
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
                outputdata = f.readlines()
                fileExist = "true"

                # ProxyServer finds a cache hit and generates a response message
                # Send the file data to the client
                tcpCliSock.send("HTTP/1.0 200 OK\r\n")
                tcpCliSock.send("Content-Type:text/html\r\n\r\n")
                # TODO start.
                for i in range(0, len(outputdata)):
                    connectionSocket.send(outputdata[i].encode())
                connectionSocket.send("\r\n".encode())
                # TODO end.

                print('Read from cache')
        # Error handling for file not found in cache
        except IOError:
                if fileExist == "false":
                        # Create a socket on the proxyserver
                        c = # Fill in start.            # Fill in end.
                        hostn = filename.replace("www.","",1)
                        print(hostn)
                        try:
                                # Connect to the socket to port 80
                                # TODO start.

                                # TODO end.

                                # Create a temporary file on this socket and ask port 80 for the file requested by the client
                                fileobj = c.makefile('r', 0)
                                fileobj.write("GET "+"http://" + filename + " HTTP/1.0\n\n")

                                # Read the response into buffer
                                # TODO start.

                                # TODO end.

                                # Create a new file in the cache for the requested file.
                                # Also send the response in the buffer to client socket and the corresponding file in the cache
                                tmpFile = open("./" + filename,"wb")
                                # TODO start.

                                # TODO end.
                        except:
                                print("Illegal request")
                else:
                        # HTTP response message for file not found
                        # Fill in start.
                        # Fill in end.
        # Close the client sockets
        tcpCliSock.close()
# Close the server socket
# TODO start.

# TODO end.
