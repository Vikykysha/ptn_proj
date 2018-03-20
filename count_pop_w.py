from collections import Counter

with open('file_ord.txt', 'r') as f:

    read_data = f.readlines()
    
read_data = ' '.join(read_data)
read_data = Counter(map(str.lower,[x.strip('!.,?')  for x in read_data.split(' ') if x != '' and len(x)>3])).most_common(3)
print("The most common word is  \"%s\".It has %d counts" % (read_data[0][0], read_data[0][1]))
