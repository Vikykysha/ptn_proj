#Подсчет количества каждой из букв, встречающихся в предлоежнии

str = "This is an example"

count = {}
for i in str:
    count.setdefault(i,0)
    count[i] = count[i] + 1
print(count)
