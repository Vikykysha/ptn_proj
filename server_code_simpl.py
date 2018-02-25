#создание сокета, контекстный менеджер
#сервер

import socket

with socket.socket() as sock:
    sock.bind(("", 10001))
    sock.listen()

    while True:
        conn, addr = sock.accept()
        print("connection addr: ", addr)
        conn.settimeout(5) #вызовется после получения соеденения из предыдущей строки
        with conn:
            while True:
                try:
                    data = conn.recv(1024) #если в теение 5 секунд не поступило данных, то вызовется исключение 
                except socket.timeout:
                    print("Close connection by timeout")
                    break
                
                if not data:
                    break
                print(data.decode("utf8"))