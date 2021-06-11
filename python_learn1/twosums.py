x = [3,4,7,8,12]
target = 12
found = False

for j in range(len(x)-1):
    for i in range(1, len(x) - 1):
        if x[j] + x[i] != target:
            continue
        else:
            found = True
            break
    if found == True:
        break

if found == True:
    print ("Found", j, i)
else:
    print ("Not Found")
