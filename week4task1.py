import os, sys, tempfile
import random

"""Реализация собственного класса файла"""

class File:
    def __init__(self,path):
        self.path = os.path.join(os.getcwd(), path)
        
    def write(self,line):
        with open(self.path, 'a') as f:
            f.write(line)

    def __add__(self, ob):
        tmp = os.path.join(tempfile.gettempdir(),str(random.random()))
        ob_new = File(tmp)
        t = ""
        t1 = ""
        try:
            with open(self.path,  'r') as f1, open(ob.path, 'r')  as f2:
                t = f1.read()
                t1 = f2.read()       
        except IOError:
            return ""
        try:
            with open(ob_new.path,'a') as ff:
                ff.write(t)
                ff.write(t1)
                return ob_new
        except IOError:
            return ""
    def __iter__(self):
        with open(self.path,'r') as f:
            self.len_cont = f.readlines()
            self.cnt = 0
        return self
    def __next__(self):
        
        if len(self.len_cont) <= self.cnt:
            self.cnt = 0
            raise StopIteration
        else:
            a = self.len_cont[self.cnt]
            self.cnt +=1
            return a              
    def __str__(self):
        return self.path
    
    def __del__(self):
        os.remove(self.path)


'''

#Для проверки:

f1 = File("tmp1.txt")
f2 = File("tmp2.txt")
f1.write("")
f2.write("")
f1.write("")
c = f1 + f2

for line in c:
    print(line)

'''

