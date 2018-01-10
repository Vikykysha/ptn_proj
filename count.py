inv = {'rope' : 1, 'torch' : 6, 'gold_coin' : 42, 'dagger' : 1, 'arrow' : 12}

print('Inventory: ', end = '\n')

def displayInv(invent):
    count = 0
    for k,v in invent.items():
        print(str(v) + ' ' + k, end = '\n')
        count = count + v
    return count
count = displayInv(inv)
print('Total number of items: ' + str(count))

dragonLoot = ['dragon_coin', 'dagger', 'gold_coin', 'gold_coin', 'ruby']

def addToInv(inv,lst):
    for i in lst:
        inv.setdefault(i,0)
        inv[i] = inv[i] + 1
    return inv

inv_upd = addToInv(inv,dragonLoot)

displayInv(inv_upd)
