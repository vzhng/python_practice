fp = open("filelines.txt")
fout = open("filelines_out.txt", "w")
def mycap(s):
    s3 = []
    s4 = s.split()
    for word in s4:
        s5 = word.capitalize()
        s3.append(s5)
    return " ".join(s3)

s1 = fp.readline()
while (s1 != ""):
    #s2 = s1.upper()
    s2 = mycap(s1)
    print(s2)
    fout.write(s2 + "\n")
    s1 = fp.readline()

fp.close()
fout.close()


