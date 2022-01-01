# https://programmers.co.kr/learn/courses/30/lessons/77884

-----Mine-----
def getMyDivisor(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return divisorsList

def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        if len(getMyDivisor(n)) % 2 == 0:
            answer += n
        else:
            answer -= n
    
    return answer

-----Others-----
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer
