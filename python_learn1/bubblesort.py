x = [3,8,4,7,2,0]

for j in range(len(x)-1):

    for i in range(len(x) - 1 - j):
        if x[i + 0] > x[i + 1]:
            z = x[i]
            x[i] = x[i + 1]
            x[i + 1] = z

print (x)
