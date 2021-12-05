# https://programmers.co.kr/learn/courses/30/lessons/12933

-----Mine-----
def solution(n):
    arr = list(map(int, str(n)))
    
    arr.sort(reverse=True)

    return int(''.join(str(num) for num in arr))

-----Others-----
def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))
