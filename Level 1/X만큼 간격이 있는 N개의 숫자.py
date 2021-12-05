# https://programmers.co.kr/learn/courses/30/lessons/12954

-----Mine-----
def solution(x, n):
    answer = [x]
    
    for i in range(n - 1):
        answer.append(answer[i] + x)
    
    return answer

-----Others-----
def number_generator(x, n):
    return [i * x + x for i in range(n)]
print(number_generator(2, 5))
