class Cont:
    def __init__(self, list_l = None):
        self.list = list_l or []
    def __getitem__(self,index):
        if len(self.list) == 0:
            return "List is empty!"
        else:
            return self.list[index]
    def __setitem__(self,index,value):
        if len(self.list) == 0 or index > len(self.list):
            self.list.append(value)
        else:
            self.list[index] = value
    def __str__(self):
        return self.list.__str__()

c = Cont()
c[3] = 2
c[0] = 1
print(c)