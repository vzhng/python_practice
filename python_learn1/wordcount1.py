
#s1 = "nba cxy word history type cxy nba history word word type type history"
s1 = input("Please input words:")
s2 = s1.split()

dict={}
for word in s2:
    print (word)
    if word in dict:
        n = dict[word]
        n = n+1
        dict[word] = n
    else:
        dict[word] = 1

print (dict)
