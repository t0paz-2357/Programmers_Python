# https://programmers.co.kr/learn/courses/30/lessons/12940

-----Mine-----
from math import gcd

def solution(n, m):
    return [gcd(n, m), n * m // gcd(n, m)]

-----Others-----
def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer
