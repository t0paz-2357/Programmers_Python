# https://programmers.co.kr/learn/courses/30/lessons/12910

-----Mine-----
def solution(arr, divisor):
    answer = []
    
    for temp in arr:
        if temp % divisor == 0:
            answer.append(temp)
    
    if len(answer) == 0:
        answer.append(-1)
    
    answer.sort()
    
    return answer

-----Others-----
def solution(arr, divisor):
    return sorted([n for n in arr if n%divisor == 0]) or [-1]
