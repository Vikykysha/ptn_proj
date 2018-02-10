import sys 

class FileReader:
    def __init__(self, p):
        self._path = p
    def read(self):
        try:
            with open(self._path,'r') as p:
                s = p.read()
        except IOError:
            return ""
        else:
            return s
        
def _main():
    path_ = sys.argv[1]
    reader = FileReader(path_)
    print(reader.read())

if __name__ == '__main__':
    _main()