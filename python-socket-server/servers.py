import os
import socket
import json

def json_parser(raw):
    try: 
        j = json.loads(raw)
    except:
        return "Not JSON Format"
    
    if 'id' in j and 'from' in j and 'to' in j and 'fizz' in j and 'buzz' in j :
        pk = j["id"]
        start = j['from']
        end = j['to']
        f = j['fizz'] 
        b = j['buzz']


        lst = []

        for d in range(start,end):
            
            d3 = d % 3
            d5 = d % 5

            if d3 == 0 and d5 == 0:
                lst.append("%s%s" % (f,b))
            elif d3 == 0 and d5 > 0:
                lst.append(f)
            elif d5 == 0 and d3 > 0:
                lst.append(b)
            else:
                lst.append(d)

        m = {pk:lst}


    else:
        m = "JSON Format {'id':<string>, 'from':<integer>, 'to':<integer>, 'fizz':<string>, 'buzz':<string>}"

    return m

def receive(conn):
    """receive and process data from connection"""
    data = conn.recv(1024)
    print("Data Recieved : %s" % data.decode('utf-8'))
    if data:
        r_dict = {}
        for raw in data.decode('utf-8').split("\\n"):
            if raw:
                d = json_parser(raw)
                if isinstance(d, dict):
                    r_dict.update(d)
                else:
                    conn.send(d.encode('utf-8'))
        
        if r_dict:
            conn.send(json.dumps(r_dict).encode('utf-8'))
       
        
        
if __name__ == "__main__":
    socket_addr = "/tmp/docker_socket.s"

    # initialize unix socket
    s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

    # bind socket address
    if os.path.exists(socket_addr):
        os.unlink(socket_addr)
    s.bind(socket_addr)

    # accept connection
    s.listen(2)
    conn, addr = s.accept()
    print("connection accepted")
    
    # receive messages and print to terminal
    while True:
        receive(conn)
        
        


