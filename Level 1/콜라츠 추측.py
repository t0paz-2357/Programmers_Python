# https://programmers.co.kr/learn/courses/30/lessons/12943

-----Mine-----
def solution(num):
    answer = 0
    
    for i in range(500):
        if i == 499:
            return -1
        
        if num == 1:
            break
        elif num % 2 == 0:
            num = num / 2
            answer += 1
        else:
            num = num * 3 + 1
            answer += 1
    
    return answer

-----Others-----
def collatz(num):
    for i in range(500):
        num = num / 2 if num % 2 == 0 else num*3 + 1
        if num == 1:
            return i + 1
    return -1
