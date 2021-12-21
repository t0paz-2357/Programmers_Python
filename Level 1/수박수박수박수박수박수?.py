# https://programmers.co.kr/learn/courses/30/lessons/12922

-----Mine-----
def solution(n):
    answer = ''
    arrStr = ['수', '박']
    
    for i in range(n):
        answer += arrStr[i % 2]
    
    return answer

-----Others-----
def water_melon(n):
    s = "수박" * n
    return s[:n]
