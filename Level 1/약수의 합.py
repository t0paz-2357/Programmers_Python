# https://programmers.co.kr/learn/courses/30/lessons/12928

-----Mine-----
def solution(n):
    temp = []
    
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            temp.append(i)
            if ((i ** 2) != n):
                temp.append(n // i)
    
    return sum(temp)

-----Others-----
def sumDivisor(num):
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])
