x = [3,5,24,4,150,112]
y = input("Please input a number: ")
z = int(y)

x.sort()
print (x)

def binarysearch(x:list,y:int):
    found = False
    left = 0
    right = len(x)-1
    while not found:
        mid = int((right + left) / 2)
        if x[mid] > y:
            right = mid
        elif x[mid] < y:
            left = mid
        elif x[mid] == y:
            found = True
        elif right - left <= 1:
            return -1
    return mid

m = binarysearch(x,z)
print (m)

