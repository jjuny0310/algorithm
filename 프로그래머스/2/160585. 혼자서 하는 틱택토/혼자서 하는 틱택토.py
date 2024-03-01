from itertools import permutations

def is_end(now):
    if now[0] != "." and now[0] == now[1] == now[2]:
        return True
    elif now[3] != "." and now[3] == now[4] == now[5]:
        return True
    elif now[6] != "." and now[6] == now[7] == now[8]:
        return True
    elif now[0] != "." and now[0] == now[3] == now[6]:
        return True
    elif now[1] != "." and now[1] == now[4] == now[7]:
        return True
    elif now[2] != "." and now[2] == now[5] == now[8]:
        return True
    elif now[0] != "." and now[0] == now[4] == now[8]:
        return True
    elif now[2] != "." and now[2] == now[4] == now[6]:
        return True
    else:
        return False

    
def solution(board):
    done = set()
    
    numbers = [i for i in range(9)]
    cases = []
    for i in range(10):
        cases.extend(permutations(numbers, i))
        
    
    target = []
    for i in range(3):
        for j in range(3):
            target.append(board[i][j])
    
    for case in cases:
        now = ["."] * 9
        
        for i in range(len(case)):
            if i % 2 == 0:
                now[case[i]] = "O"
            else:
                now[case[i]] = "X"
                
            if is_end(now):
                break
        
        if target == now:
            return 1
    
    return 0