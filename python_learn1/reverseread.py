# fp = open("reverseread.txt")
# s1 = fp.readline()
# s2 = s1.split()

s2 = "Rats live on no evil star"
n = len(s2)
result = True
s2 = s2.lower()

for i in range(0,n):
    if s2[i] == s2[n-i-1]:
        continue
    else:
        result = False
        break


print (s2, result)

