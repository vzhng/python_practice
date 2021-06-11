x = "abcdef"

stack = []

def push(c):
    stack.append(c)

def pop():
    m = stack.pop(len(stack)-1)
    return m

for c in x:
    push(c)

result = ""
len2 = len(stack)
for i in range(len2):
    n = pop()
    result = result + n

print (result)