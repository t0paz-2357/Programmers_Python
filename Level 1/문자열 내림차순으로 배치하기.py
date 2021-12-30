# https://programmers.co.kr/learn/courses/30/lessons/12917

-----Mine-----
def solution(s):
    arr = list(s)    
    arr.sort(reverse=True)
    return ''.join(arr)

-----Others-----
def solution(s):
    return ''.join(sorted(s, reverse=True))
