import socket
from collections import deque

HOSTNAME = "localhost"
PORT = 8000
QUEUE_SIZE = 100000

class QueueServer:
    """
    queuer server
    """
    def __init__(self, hostname=HOSTNAME, port=PORT):
        self.hostname = hostname
        self.port = port
        self.queue = Queue.Queue(maxsize=QUEUE_SIZE)

    def start(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((HOSTNAME, PORT))
        self.sock.listen(10)
        while True:
            connection, address = sock.accept()
            try:
                connection.settimeout(60)
                buf = connection.recv(1024)
                if buf:
                    print address, buf
                    self.paraphrase(buf, connection)
                else:
                    connection.send('None')
            except socket.timeout:
                print "time out"
                connection.send("Time out")
            connection.close()

    def paraphrase(self, string, connection):
        if string == "Size":
            connection.send(str(len(len(self.queue)))
        elif string == "List":
            connectin.send(",".join(self.queue))
        elif string == "Pop":
            if len(self.queue) == 0:
                connection.send("None")
            else:
                connection.send(self.queue.popleft())
        else:
            if len(self.queue) == QUEUE_SIZE:
                connection.send("Full")
            else:
                self.queue.append(string)
                connection.send("Done")

if __name__ == "__main__":
    server = QueueServer()
    server.start()
