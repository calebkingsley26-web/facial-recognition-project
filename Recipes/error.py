def number(n):
    for i in range(1,100):
        yield (i)

for i in number(111):
    print(i)
