import socket

PORT = 8088
IP = "10.108.33.47"
MAX_OPEN_REQUESTS = 5

# RMB is the China currency: Renminbi is the currency, Yuan is the unit



def process_client(clientsocket):
    #adress[0]=direcciión IP del cliente
    #add=int(add)
    # utf8 supports all lanaguages chars
    #send_message = 'HEY'
    # Serializing the data to be transmitted
    #send_bytes = str.encode(send_message)
    # We must write bytes, not a string
    #clientsocket.send(send_bytes)
    condition = True
    while condition:
        mensaje_recibido = str(clientsocket.recv(2048).decode("utf-8"))
        print("Celia: ",mensaje_recibido)
        if mensaje_recibido == 'Adios':
            send_message ='Adios'
            condition = False
            send_bytes = str.encode(send_message)
            clientsocket.send(send_bytes)
            clientsocket.close()
        else:
            send_message =input("Mary Hope: ")
            send_bytes = str.encode(send_message)
            clientsocket.send(send_bytes)




# create an INET, STREAMing socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket to a public host, and a well-known port
# hostname = socket.gethostname()
# Let's use better the local interface name
hostname = IP
try:
    serversocket.bind((hostname, PORT))
    # become a server socket
    # MAX_OPEN_REQUESTS connect requests before refusing outside connections
    serversocket.listen(MAX_OPEN_REQUESTS)

    while True:
        # accept connections from outside
        print("Waiting for connections at %s %i" % (hostname, PORT))
        (clientsocket, address) = serversocket.accept()

        # now do something with the clientsocket
        # in this case, we'll pretend this is a non threaded server
        process_client(clientsocket)

except socket.error:
    print("Problemas using port %i. Do you have permission?" % PORT)
