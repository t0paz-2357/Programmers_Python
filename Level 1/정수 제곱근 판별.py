# https://programmers.co.kr/learn/courses/30/lessons/12934

-----Mine-----
import math

def solution(n):
    temp = math.sqrt(n)
    
    if int(temp) == temp:
        return pow(int(temp) + 1, 2)
    else:
        return -1

-----Others-----
def nextSqure(n):
    return n == int(n**.5)**2 and int(n**.5+1)**2 or 'no'
