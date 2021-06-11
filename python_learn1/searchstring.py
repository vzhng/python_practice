fp = open("filelines.txt")
s1 = fp.readline()
userMatch = "We"

def searchline(s: str, match: str):
    count = 0
    s2 = s.split()
    for word in s2:
        if word.lower() == match.lower():
            count = count + 1
    return count

matchcount = 0

while s1 != "":
    print (s1)
    c = searchline(s1, userMatch)
    matchcount = matchcount + c
    s1 = fp.readline()

print("Found total count=", matchcount)
fp.close()
