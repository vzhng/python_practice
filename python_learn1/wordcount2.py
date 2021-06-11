fp = open("wordcount2.txt")
s1 = fp.read()
fp.close()

s2 = s1.split()

dict = {}
for word in s2:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1

print (dict)



