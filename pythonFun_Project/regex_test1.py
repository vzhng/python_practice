import re
x = "Ver is 2.3"
res = re.search ("^Ver.*2.3$", x)
#print (res)

x = "Ver is 2.33"
res2 = re.search ("^Ver.*\s([\.\d]+)$", x)
# print (res2)
# print(res2.group(0))
# print(res2.group(1))

x = "2.33 + 3.45"
res3 = re.match ("^([\.\d]+)\s*([\+\-\*/])\s*([\.\d]+)", x)
print (res3.group(0))
print (res3.group(1))
print (res3.group(2))
print (res3.group(3))




