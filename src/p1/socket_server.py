import socket
from server_function import *

# Specify the IP addr and port number
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
# TODO start
#HOST, PORT = "127.0.0.1", 5001
HOST, PORT = "127.0.0.1", 5000

print("server IP: {}::{}".format(HOST, PORT) )
# TODO end

while(True):
    # Listen for any request

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (HOST, PORT) )
    s.listen(0)
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new request and admit the connection
        client, address = s.accept()

        print(str(address)+" connected")
        try:
            while (True):
                client.send(b"Welcom to the calculator server. Input your problem ?\n")

                # Recieve the data from the client and send the answer back to the client
                request = client.recv(1000).upper().decode('utf-8')
                client.send("Answer: {}\n".format(parse_request(request)).encode('utf-8'))

                # Ask if the client want to terminate the process
                # Terminate the process or continue
                response = ""
                while (True):
                    client.send(b"Do you have any more question?(y/n)")
                    response = client.recv(1000).upper().decode('utf-8')
                    if(response == "Y" or response == "N" ):
                        break

                if( response == "N" ):
                    client.send(b"Bye Bye")
                    client.close()
                    break

                # TODO end
        except ValueError:
            print("except")

        break
    s.close()
    break

