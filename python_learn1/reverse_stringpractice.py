x = "abcdef"
stack = []

def push(m):
    stack.append(m)

def pop():
    y = stack.pop(len(stack)-1)
    return y

for c in x:
    push(c)

result = ""
for c in x:
    n = pop()
    result = result + n

print (result)