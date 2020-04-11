import socket
from server_function import *
from send_read_function import *

# Specify the IP addr and port number
# (use "127.0.0.1" for localhost on local machine)
# Create a socket and bind the socket to the addr
HOST, PORT = "127.0.0.1", 5000
print("server IP: {}::{}".format(HOST, PORT) )

while(True):
    # Listen for any client_msg
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind( (HOST, PORT) )
    s.listen(0)
    print("The Grading server for HW2 is running..")

    while(True):
        # Accept a new client_msg and admit the connection
        client, address = s.accept()

        print(str(address)+" connected")
        try:
            while (True):
                server_msg = "Welcom to the calculator server. Input your problem ?"
                socket_send( client, server_msg)

                # Recieve the data from the client and send the answer back to the client
                client_msg = socket_read( client )

                answer = parse_request(client_msg)
                socket_send( client, "Answer: {}".format(answer) )

                # Ask if the client want to terminate the process
                # Terminate the process or continue
                client_msg = ""
                while (True):
                    server_msg = "Do you have any more question? (Y/N)"
                    socket_send( client, server_msg)

                    client_msg = socket_read( client ).upper()
                    if(client_msg == "Y" or client_msg == "N" ):
                        break

                if( client_msg == "N" ):
                    server_msg = "Close connection."
                    socket_send( client, server_msg)
                    client.close()
                    break
        except ValueError:
            print("except")
        break
    print("Close socket server.")
    s.shutdown(socket.SHUT_RDWR)
    s.close()
    break

