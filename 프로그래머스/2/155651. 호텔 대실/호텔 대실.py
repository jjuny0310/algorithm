from collections import deque


def solution(book_time):
    new_book_time = []
    for i in range(len(book_time)):
        s_h, s_m = map(int, book_time[i][0].split(":"))
        e_h, e_m = map(int, book_time[i][1].split(":"))
        new_book_time.append([60*s_h + s_m, 60*e_h + e_m])
    book_time = new_book_time
    book_time.sort(key=lambda x:x[0])
    
    answer = 1
    reserve = [book_time[0][1] + 10]
    for s_m, e_m in book_time[1:]:
        new_reserve = []
        for r_m in reserve:
            if r_m > s_m:
                new_reserve.append(r_m)
        reserve = new_reserve
        reserve.append(e_m + 10)
        answer = max(answer, len(reserve))
    
    return answer