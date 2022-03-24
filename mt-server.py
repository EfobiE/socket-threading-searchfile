import time, _thread as thread           # or use threading.Thread().start()
from socket import *                     # get socket constructor and constants
from searchfile import search
myHost = ''                              # server machine, '' means local host
myPort = 50007                           # listen on a non-reserved port number

sockobj = socket(AF_INET, SOCK_STREAM)           # make a TCP socket object
sockobj.bind((myHost, myPort))                   # bind it to server port number
sockobj.listen(5)                                # allow up to 5 pending connects

def now():
    return time.ctime(time.time())               # current time on the server

def handleClient(connection):                    # reply
    time.sleep(5)                                # simulate latency
    data = connection.recv(1024)    #data = recieved key w/ wildcard
    recved = data.decode()  #holds recieved query data from client
    reply = search(recved)  #reply = list of words from wordlist searched through with recved
    for line in reply:      #sends reply word by word
        connection.send(line.encode())
    print("connection closed")
    connection.close()

def dispatcher():                                # listen until process killed
    while True:                                  # wait for next connection,
        connection, address = sockobj.accept()   # pass to thread for service
        print('Server connected by', address, end=' ')
        print('at', now())
        thread.start_new_thread(handleClient, (connection,))

dispatcher()
