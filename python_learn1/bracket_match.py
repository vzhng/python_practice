# x = "{(ab)}"
# x = "[{(ab)"
x = "{ab[(jk])"
stack = []

pair = True
bracketleft = ["[", "{", "("]
bracketright = ["]", "}", ")"]
for c in x:
    if c in bracketleft:
        stack.append(c)
    elif c in bracketright:
        if stack[len(stack)-1] == "{" and c == "}":
            stack.pop()
        if stack[len(stack)-1] == "[" and c == "]":
            stack.pop()
        if stack[len(stack)-1] == "(" and c == ")":
            stack.pop()
        else:
            pair = False
            break
    else:
        continue

if len(stack) != 0:
    pair = False

print (pair)
