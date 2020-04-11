import socket
from send_read_function import *

# Specify the IP addr and port number
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
HOST, PORT = "127.0.0.1", 5000
print("Connect to IP: {}::{}".format(HOST, PORT) )

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect( (HOST, PORT) )
except ConnectionRefusedError:
    print("Connection refused")

while( True ):
    try:
        response = socket_read(s)

        if response == '':
            raise
        print(response)

        if response == "Welcom to the calculator server. Input your problem ?":
            # Ask question
            request = input("Input: ")
            socket_send(s, request)

            response = socket_read(s)
            if response == '':
                raise
            print(response)
        elif response == "Do you have any more question? (Y/N)":
            # Response
            request = input()
            socket_send(s, request)
        elif response == "Close connection.":
            s.close()
            break
        else:
            print("Undefined behavior")
            exit(1)
    except:
        print("Connection closed.")
        break

