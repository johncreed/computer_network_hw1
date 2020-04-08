import socket

# Specify the IP addr and port number
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
#HOST, PORT = "127.0.0.1", 5001
HOST, PORT = "127.0.0.1", 5000

print("client IP: {}::{}".format(HOST, PORT) )
# TODO end

# Listen for any request
# TODO start

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect( (HOST, PORT) )
except ConnectionRefusedError:
    print("Connection refused")

while( True ):
    response =  s.recv(1000).decode('utf-8')
    print(response)
    try:
        request = input().encode('utf-8')
        s.send(request)
    except BrokenPipeError:
        print("Connection closed.")
        break
