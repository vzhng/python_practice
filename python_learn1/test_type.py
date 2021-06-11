x = "30"
x = 30
y = x + 5.
z = complex (real=3, imag=5)

print(y)
print (type(y))

x = "awesome"

def minmax(arr) -> (int, int):
    return (3, 5)

(a, b) = minmax(x)

def myfunct():
    global x
    x = "fantastic"
    print (x)

myfunct()
print (x)

y = x
# print(x, y)

a = "Hello, World!"
b = a.split()
print (b[1])

mylist = ["apple", "banana", "orange", "apple", "pear", "kiwi"]
mylist2 = mylist.copy()
mylist.remove("apple")
print (mylist)
print(mylist2)

newlist = [x for x in mylist if "a" in x]
#print (newlist)

mylist.sort()
#print(mylist)
