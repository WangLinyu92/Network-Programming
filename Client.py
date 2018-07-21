import socket
from time import ctime
HOST = 'localhost'
PORT = 8999
BUFSIZE = 8192


def main():
    ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ClientSocket.connect((HOST, PORT))
    while True:
        data = input("input> ")
        if not data:
            break
        ClientSocket.send(data.encode())
        data = ClientSocket.recv(BUFSIZE)
        if not data:
            break
        print(data.decode('utf-8'))
    ClientSocket.close()


if __name__ == "__main__":
    main()
