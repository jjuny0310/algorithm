n = int(input())
arr = list(map(int, input().split()))
s = int(input())

front = 0
while True:
    if s == 0 or front > n:
        break

    temp = []
    for idx in range(front + 1, n):

        if arr[front] < arr[idx] and idx - front <= s:
            temp.append([arr[idx], idx])

    temp.sort(key=lambda x: -x[0])
    if temp:
        idx = temp[0][1]
        arr.insert(front, arr.pop(idx))
        s -= idx - front
    front += 1

print(" ".join(map(str, arr)))