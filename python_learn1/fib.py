
m=input("Please input a number:")

#m=100
def fib(n):
    a1=1
    a2=0
    an=1
    while an < n:
        ax = a1 + a2
        if ax > n:
            break
        an = ax
        a2 = a1
        a1 = an
    return an
x=fib(int(m))
print(x)
