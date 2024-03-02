def solution(numbers):
    numbers.reverse()
    
    answer = []
    stack = []
    for i in range(len(numbers)):
        now = numbers[i]
        
        while stack:
            if stack[-1] > now:
                answer.append(stack[-1])
                stack.append(now)
                break
            else:
                stack.pop()
                
        else:
            stack.append(now)
            answer.append(-1)    

    return answer[::-1]