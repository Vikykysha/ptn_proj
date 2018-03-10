import socket
import time
from collections import defaultdict

class ClientError(Exception):
    pass

class Client:
    time = time.time()
    def __init__(self,host,port,timeout  = None):
        self._host = host
        self._port = port
        self._timeout = timeout

    def put(self,key,value,timestamp =  time):
        with socket.create_connection((self._host,self._port)) as sock:           
            data = 'put {} {} {}\n'.format(key, str(value), str(int(timestamp)))
            try:            
                sock.sendall(data.encode("utf8"))
                answer = sock.recv(1024).decode("utf8")
                if answer != "ok\n\n":
                    raise ClientError   		             
            except socket.error:
                raise ClientError  
                   
    def get(self,key):
        dict_data = defaultdict(list)
        with socket.create_connection((self._host,self._port)) as sock:
            sock.settimeout(3)
            message = 'get %s\n' % (key)
            try:
                sock.sendall(message.encode("utf8"))               
            except socket.error:
                raise ClientError
            data = sock.recv(1024)
            data = data.decode("utf8")
        if  data == 'ok\n\n':
            return {}
        data = data.lstrip('ok\n').rstrip('\n\n')
        data = [x.split() for x in data.split('\n')]
        l = len(data)
        for i in range(l):
            dict_data[data[i][0]].append([])
            ll = len(dict_data[data[i][0]]) 
            dict_data[data[i][0]][ll - 1].append(int(data[i][2])) 
            dict_data[data[i][0]][ll - 1].append(float(data[i][1]))  
            dict_data[data[i][0]][ll - 1] = tuple(dict_data[data[i][0]][ll - 1])
        return dict(dict_data)
        
            
            


    

    
