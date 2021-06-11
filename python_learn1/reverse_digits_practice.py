x = [1,2,3,4,5,6,7,8]
import math

for i in range(len(x)):
    m = x[len(x)-1-i]
    x[len(x)-1-i] = x[i]
    x[i] = m
    if i == math.floor(len(x)/2):
        break

print (x)