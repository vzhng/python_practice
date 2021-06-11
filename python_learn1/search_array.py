x = [11,23,58,31,56,77,43,12,65,19]
y = input("Please input number:")
z = int(y)

x.sort()
print (x)

def binarysearch(x:list,y:int):
    found = False
    leftIndex = 0
    rightIndex = len(x)-1
    while not found:
        midIndex = int((rightIndex + leftIndex)/2)
        #midIndex = int(midIndex)
        if x[midIndex] > y:
            rightIndex = midIndex
        elif x[midIndex] < y:
            leftIndex = midIndex
        elif x[midIndex] == y:
            found = True
        elif rightIndex - leftIndex <= 1:
            return -1
    return midIndex

p = binarysearch(x,z)
print (p)