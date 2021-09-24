import socket

def send(s):
    """send message on socket connection"""
    cmd = input("Send message:")
    s.send(cmd.encode("utf-8"))
    data = s.recv(1024)
    print("Response : %s" % data.decode('utf-8'))
    
    
if __name__ == "__main__":
    socket_addr = "/tmp/docker_socket.s"

    # initialize unix socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # connect to socket at address
    s.connect(socket_addr)

    # send messages over socket
    while True:
        send(s)




