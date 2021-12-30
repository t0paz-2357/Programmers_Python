# https://programmers.co.kr/learn/courses/30/lessons/12903

-----Mine-----
def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        answer += s[len(s) // 2 - 1] + s[len(s) // 2]
    else:
        answer += s[len(s) // 2]
        
    return answer

-----Others-----
def string_middle(str):
    return str[(len(str)-1)//2:len(str)//2+1]
