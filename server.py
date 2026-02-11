import socket
from _thread import *

server = "0.0.0.0"  
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server Started! Waiting for connection...")

pos = [(0, 0), (100, 100)]    


def readPose(pos_str):
    try:
        x, y = pos_str.split(",")
        return int(x), int(y)
    except:
        return 0, 0


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])


def threaded_client(conn, player):
    conn.send(str.encode(makePos(pos[player])))

    while True:
        try:
            data = conn.recv(2048).decode()

            if not data:
                print("Disconnected")
                break

            data = readPose(data)
            pos[player] = data

            if player == 0:
                reply = pos[1]
            else:
                reply = pos[0]

            conn.sendall(str.encode(makePos(reply)))

        except:
            break

    print("Lost connection")
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer = (currentPlayer + 1) % 2   # prevents index error
