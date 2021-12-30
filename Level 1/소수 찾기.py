# https://programmers.co.kr/learn/courses/30/lessons/12921

-----Mine-----
import math

def isPrime(num):
    if num == 2:
        return True

    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False

    return True

def solution(n):
    answer = 0

    for i in range(2, n + 1):
        if isPrime(i) == True:
            answer += 1

    return answer 

-----Others-----
def solution(n):
    # 2부터 n+1까지의 집합
    num=set(range(2,n+1))

    for i in range(2,n+1): # 2부터 n까지 반복문
        if i in num: # 만약 i가 num 집합에 있다면
            num-=set(range(2*i,n+1,i)) # i의 배수는 num 집합에서 제외
    return len(num) # num에 남아있는 숫자의 개수가 소수의 개수
