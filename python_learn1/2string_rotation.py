# f1 = open("2string_rotation.txt")
# firstline = f1.readline()
# s1 = firstline.split()
# secondline = f1.readline()
# s2 = secondline.split()

s1 = "abcde"
s2 = "cdeab"

s3 = s2 * 2
print (s3)

userMatch = s1

def search(s3:str, userMatch:str) -> (bool, int):
    match = False
    atIdx = -1
    for i,c in enumerate(s3):
        substr = s3[i:i+len(userMatch)]
        if compareTwoStr(substr, userMatch):
            match = True
            atIdx = i
            break
    return (match, atIdx)


def compareTwoStr(s1: str, s2: str) -> bool:
    match = True
    for i in range(len(s1)):
        character1 = s1[i]
        character2 = s2[i]
        if character1 != character2:
            match = False
            break
    return match

(x, idx) = search(s3, userMatch)
print (x, idx)

# match = True
# if len(s1) != len(s2):
#     match = False
#
# for i in range(len(s1)):
#     character1 = s1[i]
#     character2 = s2[i]
#     if character1 != character2:
#         match = False
#         continue
#     else:
#         break
#print (match)















