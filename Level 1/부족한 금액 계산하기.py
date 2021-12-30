# https://programmers.co.kr/learn/courses/30/lessons/82612

-----Mine-----
def solution(price, money, count):
    sum = 0
    
    for i in range(1, count + 1):
        sum += price * i
    
    answer = money - sum
    
    if answer < 0:
        return -1 * answer
    else:
        return 0

-----Others-----
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)
