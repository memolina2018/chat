
import socket

IP = "10.108.33.47"
PORT = 8085

def mi_logica(serversocket):
    while True:
        mensaje_cliente=input("mi mensaje es: ")
        send_message = mensaje_cliente
        send_bytes = str.encode(send_message)
        s.send(send_bytes)

        mensaje=(s.recv(2048).decode("utf-8"))
        print(mensaje)
        if str(mensaje)=='Adios':
            send_message='Adios'
            send_bytes = str.encode(send_message)
            s.send(send_bytes)
            s.close()
            break

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((IP, PORT))
    mi_logica(s)
except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))


    # utf8 supports all lanaguages chars
    # Serializing the data to be transmitted
