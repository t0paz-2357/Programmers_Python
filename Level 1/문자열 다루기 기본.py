# https://programmers.co.kr/learn/courses/30/lessons/12918

-----Mine-----
def solution(s):
    if len(s) == 4 or len(s) == 6:
        return s.isdigit()
    return False

-----Others-----
def alpha_string46(s):
    return s.isdigit() and len(s) in (4, 6)
