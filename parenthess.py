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

#prnt = '(()((()()))()()'
prnt = input()
st = Stack()
balance_ = True
for i in prnt:
    if i == '(':
        st.push(i)
    else:
        if not st.is_empty():
            k = st.pop()
            if not st.is_empty():
                if st.peek() != '(':
                    balance_ = False
                    break
            else:
                balance_ = False
                break
if not st.is_empty():
    balance_ = False
print(balance_)

#Улушенный вариант

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        i = symbol_string[index]
        if i == '(':
            s.push('(')
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()
        index += 1

    if s.is_empty() and balanced:
        return True
    else:
        return False


