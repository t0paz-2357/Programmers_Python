# https://programmers.co.kr/learn/courses/30/lessons/68644

-----Mine-----
from itertools import combinations

def solution(numbers):
    answer = []
    
    numList = list(combinations(numbers, 2))
    
    for temp in numList:
        if sum(temp) not in answer:
            answer.append(sum(temp))
    
    answer.sort()
    
    return answer

-----Others-----
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))
