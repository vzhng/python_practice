x = input("Please input numbers:")
m = x.split()
dict = {}

for j in range(0,len(m)):
    mj = m[j]
    for i in range(j+1,len(m)):
        if m[i] == mj:
            if mj in dict:
                dict[mj] = dict[mj] + 1
            else:
                dict[mj] = 1
            print("found duplicate:", mj, " at index:(", i, j, ")")
print (dict)

max = 0
for r in dict:
    z = dict[r]
    if z > max:
        max = z
        maxitem = r
print (maxitem,max)
