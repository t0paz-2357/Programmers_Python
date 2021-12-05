# https://programmers.co.kr/learn/courses/30/lessons/12931

-----Mine-----
def solution(n):
    return sum(list(map(int, str(n))))

-----Others-----
def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)
