a=[5, 1, 3, 9, 10, "hello", 10.43, [1, 3, 4, 5]]
print(a)
for i in range(0,len(a)):
    print(i, a[i])

def mySort(data):
    for i in range(0,len(data)-1):
        if data[i] > data[i+1]:
            t = data[i]
            data[i]=data[i+1]
            data[i+1]=t
    return data

print(a)
b = mySort(a)
print(b)


c=[459,324,3459,9876,364,23585,12]
mySort(c)
print(c)


