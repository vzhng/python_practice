x = [1,2,3,4,5,6,7]
import math

# def reverseread(x):
#     m = []
#     for i in range(0,len(x)):
#         m = x[0]
#         x[0] = x[2]
#         x[2] = m
#     return x
#
# y = reverseread(x)
# print (y)

for i in range(len(x)):
    m = x[len(x)-1-i]
    x[len(x) - 1 - i] = x[i]
    x[i] = m
    if i == math.floor(len(x)/2):
        break

print (x)


