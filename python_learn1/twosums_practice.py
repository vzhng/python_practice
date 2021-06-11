x = [4,5,7,12,13]
target = 19

found = False

for j in range(len(x)):
    for i in range(0, len(x)):
        if x[i] + x[i + 1] != target:
            continue
        else:
            found = True
            break

if found == True:
    print ("Found")
else:
    print ("Not Found")

