# https://programmers.co.kr/learn/courses/30/lessons/12947

-----Mine-----
def solution(x):
    temp = []
    temp = list(str(x))
    
    sum = 0
    
    for i in temp:
        sum += int(i)
    
    if x % sum != 0:
        return False
    else:
        return True

-----Others-----
def Harshad(n):
    return n % sum([int(c) for c in str(n)]) == 0
