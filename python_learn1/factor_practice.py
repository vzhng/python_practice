x = int(24)

def factorfunc(n):
    m = []
    for i in range(1, n+1):
        if x % i == 0:
            m.append(i)
    return m

y = factorfunc(x)
print (y)

