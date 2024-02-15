import socket

def delayed_nc_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Server listening on {}:{}".format(host, port))

    client_socket, addr = server_socket.accept()
    print("Accepted connection from {}:{}".format(addr[0], addr[1]))

    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received from client {}: {}".format(addr[0], data.decode('utf-8')))

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    host = "10.13.200.62"
    port = 6969

    while True:
        delayed_nc_server(host, port)
