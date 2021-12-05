# https://programmers.co.kr/learn/courses/30/lessons/12932

-----Mine-----
def solution(n):
    arr = list(map(int, str(n)))
    
    temp = []
    
    for i in range(len(arr) - 1, -1, -1):
        temp.append(arr[i])

    return temp

-----Others-----
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
