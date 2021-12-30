# https://programmers.co.kr/learn/courses/30/lessons/12915

-----Mine-----
def solution(strings, n):
    strings.sort()
    strings.sort(key=lambda x:x[n])
    return strings

-----Others-----
def strange_sort(strings, n):
    return sorted(strings, key=lambda x: x[n])
