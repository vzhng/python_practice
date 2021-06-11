x = "abab"
y = "ab*"

CurrentYIdx = 0
def getNextYChar():
    global CurrentYIdx
    if y[CurrentYIdx] != "*":
        CurrentYIdx = CurrentYIdx + 1
        return y[CurrentYIdx-1]
    else:
        return y[CurrentYIdx-1]

# m = getNextYChar()
# n = getNextYChar()
# print (n,m)

match = True
for c in x:
    if c == getNextYChar():
        continue
    else:
        match = False
        break

print (match)
 


