# https://programmers.co.kr/learn/courses/30/lessons/12926

-----Mine-----
def solution(s, n):
    answer = ''
    
    for temp in s:
        if temp == " ":
            answer += " "
        elif ord(temp) >= 65 and ord(temp) <= 90:
            if (ord(temp) + n) > 90:
                answer += chr(ord(temp) + n - 26)
            else:
                answer += chr(ord(temp) + n)
        else:
            if (ord(temp) + n) > 122:
                answer += chr(ord(temp) + n - 26)
            else:
                answer += chr(ord(temp) + n)
    
    return answer

-----Others-----
def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)
