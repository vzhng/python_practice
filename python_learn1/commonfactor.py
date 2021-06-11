
a=input("Please input two numbers:")
aa=a.split()
n=int(aa[0])
m=int(aa[1])

def commonfactor(n,m):
    b=[]
    c=n
    if n>m:
        c=m
    for i in range(1,c):
        if m % i ==0 and n % i ==0:
            b.append(i)
    return b
x=commonfactor(n, m)
print(x)
