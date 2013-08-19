import socket

HOSTNAME = "localhost"
PORT = 11235

class QueueClient:
"""
test for queueserver client
"""
    def __init__(self, hostname=HOSTNAME, port=PORT):
        self.hostname = hostname
        self.port = port

    def push(self, message):
        output = self.communicate(message)
        if output == "Done":
            return True
        else:
            return False

    def pop(self):
        output = self,communicate("Pop")
        if output and output != "None":
            return output
        else:
            return ""

    def queue_size(self):
        output = self.communicate("Size")
        return output

    def queue_list(self):
        return self.communicate("List")

    def communicate(self, input):
        sock = socket.socket(socket.AF_INET. socket.SOCK_STREAM)
        try:
            sock.connect((self.hostname, self.port))
            sock.send(input)
            result = sock.recv(1024)
            sock.close()
            return resuilt
        except Exception, e:
            print e.strerror
            sock.close()
            return ""
