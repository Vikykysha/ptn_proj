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

def symbols_cheking(str):
    s = Stack()
    balanced = True
    index = 0
    while index < len(str) and balanced:
        i = str[index]
        if i in '{[(':
            s.push(i)
        else:
            if s.is_empty():
                balanced = False
            else:
                p = s.pop()
                if p != i:
                    balanced = False
        index += 1
        if balanced and s.is_empty():
            return True
        else:
            return False
