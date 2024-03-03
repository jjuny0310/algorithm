def solution(data, col, row_begin, row_end):
    answer = 0
    
    data.sort(key=lambda x:(x[col-1], -x[0]))
    
    s = []
    for i in range(row_begin - 1, row_end):
        res = 0
        for value in data[i]:
            res += value % (i+1)
        s.append(res)
    
    answer = 0
    for value in s:
        answer ^= value

    return answer