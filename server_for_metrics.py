import asyncio

storage = []

class ClientServerProtocol(asyncio.Protocol):
    data=[]
    def __init__(self):
        self._transport = None

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        res = data.decode()[:-1].split(' ')
        info = res[1:]
        if res[0] == 'put':
            resq = self._put(info)
        elif res[0] == 'get':
            resq = self._get(info)
        else:
            resq = 'error\nwrong command\n\n'
        self.transport.write(resq.encode())
    
    @staticmethod
    def _get(info):
        s = "ok\n"
        
        if len(info) != 1:
            return 'error\nwrong command\n\n'
        info = info[0].rstrip('\n')
        if info == "*":
            for i in storage:
                
                i = ' '.join(i)
                s += i + '\n'
        else:
            for i in storage:
                if info in i:
                    
                    i = ' '.join(i)
                    s += i + '\n'
        return s + '\n'

    @staticmethod
    def _put(info):
        if len(info) != 3:
            return 'error\nwrong command\n\n'
        data = list(filter(lambda x: x == info, storage))
        if len(data) == 0:
            storage.append(info)
        return 'ok\n\n'



def run_server(host, port):

    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        str(host), int(port)
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

if  __name__ == "__main__":
    run_server("127.0.0.1", 8888)


