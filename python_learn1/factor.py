a=input("Please input a number:")
#a=30
# m=int(a)

def factorize(n):
    b=[]
    for i in range(1,n+1):
        if n % i ==0:
            b.append(i)
    return b

x=factorize(int(a))
print(x)

