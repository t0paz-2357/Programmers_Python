# https://programmers.co.kr/learn/courses/30/lessons/12916

-----Mine-----
def solution(s):
    if (s.count('p') + s.count('P')) == (s.count('y') + s.count('Y')):
        return True
    return False

-----Others-----
def numPY(s):
    return s.lower().count('p') == s.lower().count('y')
