a = input("Please input two numbers:")
b = a.split()
n = int(b[0])
m = int(b[1])

def gcf(n,m):
    c = []
    b = n
    max = 1
    if n>m:
        b = m
    for i in range(1,b+1):
        if m % i == 0 and n % i ==0:
            c.append(i)
            if i>max:
                max = i
    return max

x = gcf(n,m)
print (x)