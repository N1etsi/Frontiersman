import socket
from _thread import *
import sys
from player import Player
import pickle
import numpy as np

server="172.18.0.101"
port=80

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for a connection, Server Started")



# players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]
players = []

def threaded_client(conn, player):
    players.append(Player(0,0,50,50,(round(np.random.rand()*255),round(np.random.rand()*255),round(np.random.rand()*255))))
    conn.send(pickle.dumps(players[player]))
    reply=""
    while True:
        try:
            data=pickle.loads(conn.recv(2048))
            players[player]=data

            if not data:
                print("Disconnected")
                break
            else:
                reply=[]
                for otherPlayerId in range(len(players)):
                    if otherPlayerId!=player:
                        reply.append(players[otherPlayerId])
                print("Received: ", data)
                print("Sending: ", reply)

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print("Lost Connection")
    conn.close()


currentPlayer=0
while True:
    conn,addr=s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn,currentPlayer))
    currentPlayer+=1
