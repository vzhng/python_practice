s1 = "abcde"
s2 = "abced"

s3 = s2 * 2

mmatch = s1

def searchcharacters (s3: str, mmatch: str):
    match = False
    for i,c in enumerate(s3):
        substring = s3 [i:i+len(mmatch)]
        if compareTwoStr (substring,mmatch):
            match = True
            break
    return match


def compareTwoStr (s1, s3):
    match = True
    for i in range(len(s1)):
        character1 = s1[1]
        character2 = s3[1]
        if character1 != character2:
            match = False
            continue
        else:
            break
    return match

x = searchcharacters(s3, mmatch)

print (x)
