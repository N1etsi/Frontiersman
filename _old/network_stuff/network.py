import socket
import pickle


class Network:
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server="Frontiersman.miguelnatal19.repl.co"
        self.port=80
        self.addr=(self.server, self.port)
        self.p=self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            print("Couldn't connect, probably bad port!")

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
        except EOFError:
            print("EOFError!")
