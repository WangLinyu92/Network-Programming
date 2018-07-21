import socket
from time import ctime
HOST = ''
PORT = 8999
BUFSIZE = 8192


def main():
    ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ServerAddr = (HOST, PORT)
    ServerSocket.bind(ServerAddr)
    ServerSocket.listen(5)
    while True:
        print("Waiting for connection...")
        ClientSocket, ClientAddr = ServerSocket.accept()
        print('...Connected from :', ClientAddr)
        while True:
            data = ClientSocket.recv(BUFSIZE)
            if not data:
                break
            sendstr = '[%s] %s' % (bytes(ctime(), 'utf-8'), data.decode())
            ClientSocket.send(sendstr.encode())
        ClientSocket.close()


if __name__ == "__main__":
    main()