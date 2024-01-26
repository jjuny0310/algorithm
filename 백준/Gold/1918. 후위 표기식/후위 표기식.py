s = input()

temp = ""
stack = []
for i in s:
    if i.isalpha():
        temp += i

    else:
        if i == "(":
            stack.append(i)
        elif i == ")":
            while stack:
                if stack[-1] =="(":
                    break
                temp += stack.pop()
            stack.pop()
        elif i in ["*", "/"]:
            while stack:
                if stack[-1] in ["*", "/"]:
                    temp += stack.pop()
                else:
                    break
            stack.append(i)
        elif i in ["+", "-"]:
            while stack:
                if stack[-1] == "(":
                    break
                temp += stack.pop()
            stack.append(i)

while stack:
    temp += stack.pop()

print(temp)