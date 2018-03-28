class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def divide_by_2(intg):
    t = ""
    s = Stack()
    rem = 0
    while intg != 0:
        rem = intg % 2
        if rem == 0:
            s.push(0)
        else:
            s.push(1)
        intg = intg // 2
    for _ in range(s.size()):
        t += str(s.pop())
    print(t)

divide_by_2(123)
