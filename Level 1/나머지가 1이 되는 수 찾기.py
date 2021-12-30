# https://programmers.co.kr/learn/courses/30/lessons/87389

-----Mine-----
def solution(n):
    for i in range(2, n):
        if n % i == 1:
            return i

-----Others-----
def solution(n):
    return [x for x in range(1,n+1) if n%x==1][0]
