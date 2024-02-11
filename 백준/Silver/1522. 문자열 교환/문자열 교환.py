from collections import deque

s = input()

arr = deque(sorted(s))
answer = 1e9
for _ in range(len(s)):
    count = 0
    for i in range(len(s)):
        if s[i] != arr[i]:
            count += 1
    answer = min(answer, count // 2)
    arr.append(arr.popleft())
print(answer)