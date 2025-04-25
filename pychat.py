# TODO: save everything as functions. first of all a function to connect users, another one to receive data, and another one to send it
# TODO: change mode from call recieve to host and join, leave the rest 

# My code, but my sanity depletes as it goes on

import socket # Import the library

# [VARIABLES]: Variables

connection = False

# [FUNCTIONS]: the same as always, these little shits just serve as a way to call them later. basic knowledge, if you don't understand what they do, please don't even bother reading my code.

def call(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create a socket, wich in this case would be a server
    sock.connect((ip, 12345))  # connect to the receiver
    print(f"Connected to {ip}")
    return sock

def pickUp(ip):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, 12345)) # Connect to the yapper :3
    server.listen(1) # 1 == list of users that can connect (How many people are you listening to??), socket.listen(users) for a groupchat btw
    print("Waiting for connection") # I feel like commenting on every line okay go fuck yourself
    connection, addr = server.accept()
    print("Connected by", addr) # I fucking give up this is why we can't have nice things 
    return connection, server

def send(sock):
    message = input("Type your message here: ")
    sock.sendall(message.encode())
    return

def receive(sock):
    data = sock.recv(1024)
    if data:
        print("Received:", data.decode()) # Me lo dices o me lo cuentas?
        return True
    else:
        return False

def main():
    mode = int(input("1) call, 2) receive: ")) # decide if you want to get or receive data
    ip = input("Type the ip you want to connect to: ")

    sock = None
    server = None
    if mode == 1:
        sock = call(ip)
    elif mode == 2:
        sock, server = pickUp(ip)
    else:
        print("Fuck you.")
    connection = True
    while connection:
        send(sock)
        receive(sock)
        if not connection:
            break
    sock.close() # If the loop stops, close the server
    connection.close() # if the loop stops, the connection does so, who would have guessed huh
    server.close() # this CLOSES the SERVER so uhh yea!

# [MAIN EXECUTION]: aka, the abyss
while True:
    main()

    
   