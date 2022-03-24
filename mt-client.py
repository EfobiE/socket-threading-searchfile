import time, sys,_thread as thread
from socket import * # portable socket interface plus constants
serverHost = 'localhost' # server name, or: 'starship.python.net'
serverPort = 50007 # non-reserved port used by the server
# requires bytes: b'' or str,encode()
def handleServer(userin):
    message = (x.encode() for x in userin)#encodes user input
    sockobj = socket(AF_INET, SOCK_STREAM) # make a TCP/IP socket object
    sockobj.connect((serverHost, serverPort)) # connect to server machine + port
    for line in message:
        sockobj.send(line) # send line to server over socket
    recievedData = str()
    while True:#keeps recieving data until socket is closed by server
        data = sockobj.recv(1024) # receive line from server: up to 1k
        if not data: break                      #breaks if recieved nothing
        decodedData = data.decode()#decodes encoded data from server
        recievedData = recievedData + decodedData   #adds data from server to recievedData string
    sockobj.close() # close socket to send eof to server
    print(recievedData)#prints answer to query from server
def dispatcher():                                # listen until process killed
    while True:                                  # wait for next connection,
        userin = input("Query:")#gets query  from user
        if userin == 'quit':break
        thread.start_new_thread(handleServer, (userin,))#runs handleServer on a thread
        time.sleep(6)                                # account for server blocking activity
dispatcher()
