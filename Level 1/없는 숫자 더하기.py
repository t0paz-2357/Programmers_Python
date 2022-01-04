# https://programmers.co.kr/learn/courses/30/lessons/86051

-----Mine-----
def solution(numbers):
    answer = 0
    
    for i in range(10):
        if i not in numbers:
            answer += i
    
    return answer

-----Others-----
def solution(numbers):
    return 45 - sum(numbers)
