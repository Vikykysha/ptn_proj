#Проверка строк на анаграмму
#Неэффективная реализация:
i,g = input(), input()
sl = {}
km = {}
for let in i:
    sl.setdefault(let.lower(),0)
    sl[let.lower()] += 1
for let in g:
    km.setdefault(let.lower(), 0)
    km[let.lower()] += 1
fl = True
for i in sl.keys():
    if i not in km.keys():
        fl = False
        break
    if  not sl[i] == km[i]:
        fl = False
        break
print(fl)

#Эффективная реализация
#Используем класс Counter из  класса collections.Возвращает словарь с ключами - элементами вводимого объекта, а значениями - количество этих элементов в объекте
from collections import Counter
print(Counter(input().lower()) == Counter(input().lower()))
