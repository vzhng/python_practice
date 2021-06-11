inputStr=input("Please input:")
print(inputStr)
list=inputStr.split(" ")
result=[]
for n in list:
    result.append(int(n))

print(result)
result.sort()
print(result)



