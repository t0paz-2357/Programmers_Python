# https://programmers.co.kr/learn/courses/30/lessons/12977

-----Mine-----
import math
from itertools import combinations

def solution(nums):
    answer = -1

    combi = []
    combiNum = []
    
    combi = list(combinations(nums, 3))
    
    for num in combi:
        combiNum.append(sum(num))
    
    answer = 0
    
    for num in combiNum:
        print(is_prime_num(num))
        if is_prime_num(num) == True:
            answer += 1

    return answer

def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True

-----Others-----
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
