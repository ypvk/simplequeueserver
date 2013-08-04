import socket

HOSTNAME = "localhost"
PORT = 8000
if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock .connect((HOSTNAME, PORT))
    import time
    time.sleep(2)
    sock.send("Hello")
    print sock.recv(1024)
    while True:
        pass

