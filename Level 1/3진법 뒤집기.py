# https://programmers.co.kr/learn/courses/30/lessons/68935

-----Mine-----
def changeToThree(n):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)

    return rev_base

def solution(n):
    return int(changeToThree(n), 3)

-----Others-----
def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer
