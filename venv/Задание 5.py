#Поляков, задача 256

def f(n):
    count_0 = n.count("0")
    count_1 = n.count("1")
    if count_0 == count_1:
        return n + n[len(n) - 1]
    if count_0 < count_1:
        return n + "0"
    else:
        return n + "1"

for i in range(100,200):
    x = bin(i)
    x = x[2:]
    #print(x)
    x = f(x)
    #print(x)
    x = f(x)
    #print(x)
    x = f(x)
    #print(x)
    x = "0b" + x
    x = int(x, 2)
    if x % 4 == 0 and x % 8 != 0:
        print(i)
