x = input("Please input numbers:")
p = []
m = x.split()

#for mj in m:
#for j in range(0,len(m)):
for j, mj in enumerate(m):
    for i in range(j+1,len(m)):
        if m[i] == mj:
          print("found duplicate:",mj, " at index:(",i,j, ")")


m0=m[0]
for i in range(1,len(m)):
    if m[i] == m0:
        print("found duplicate:", m0)
