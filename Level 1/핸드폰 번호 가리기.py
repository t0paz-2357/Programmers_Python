# https://programmers.co.kr/learn/courses/30/lessons/12948

-----Mine-----
def solution(phone_number):
    answer = list(phone_number)
    
    for i in range(len(answer) - 4):
        answer[i] = '*'

    return ''.join(map(str, answer))

-----Others-----
def hide_numbers(s):
    return "*"*(len(s)-4) + s[-4:]
