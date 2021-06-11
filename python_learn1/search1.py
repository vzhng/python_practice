f1 = open("filelines.txt")
find = "th"
endoffile = False

def searchprefix(line: str, prefixfind: str):
    count = 0
    s2 = line.split()
    for word in s2:
        lowerword = word.lower()
        if lowerword.startswith(prefixfind):
            count = count + 1
    return count

def searchsuffix(line: str, suffixfind: str):
    count = 0
    s2 = line.split()
    for word in s2:
        lowerword = word.lower()
        if lowerword.endswith(suffixfind):
            count = count + 1
    return count



space = 0
while not endoffile:
    s1 = f1.readline()
    if s1 == "":
        endoffile = True
    else:
        x = searchprefix(s1, find)
        space = space + x

print (x, space)
f1.close()






