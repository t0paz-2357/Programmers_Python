# https://programmers.co.kr/learn/courses/30/lessons/12906

-----Mine-----
def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            answer.append(arr[i])
        else:
            continue
    
    return answer

-----Others-----
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
