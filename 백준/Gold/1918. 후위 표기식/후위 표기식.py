prefix = input()

stack = []
postfix = ""

operator = ["+", "-", "*", "/", "(", ")"]
for i in range(len(prefix)):
    if prefix[i] not in operator:
        postfix += prefix[i]
    else:
        if prefix[i] == "(":
            stack.append(prefix[i])
        elif prefix[i] == ")":
            while stack:
                if stack[-1] == "(":
                    break
                postfix += stack.pop()
            stack.pop()
        elif prefix[i] in ["*", "/"]:
            while stack:
                if stack[-1] in ["(", "+", "-"]:
                    break
                postfix += stack.pop()
            stack.append(prefix[i])
        elif prefix[i] in ["+", "-"]:
            while stack:
                if stack[-1] == "(":
                    break
                postfix += stack.pop()
            stack.append(prefix[i])

answer = postfix + "".join(stack[::-1])
print(answer)