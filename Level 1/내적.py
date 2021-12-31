# https://programmers.co.kr/learn/courses/30/lessons/70128

-----Mine-----
def solution(a, b):
    answer = 0
    
    for i in range(len(a)):
        answer += a[i] * b[i]
    
    return answer

-----Others-----
def solution(a, b):
    return sum([x*y for x, y in zip(a,b)])
