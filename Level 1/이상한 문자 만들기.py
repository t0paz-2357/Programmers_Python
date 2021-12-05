# https://programmers.co.kr/learn/courses/30/lessons/12930

-----Mine-----
def solution(s):
    arr = list(map(str, s.split(" ")))
    
    for j in range(len(arr)):
        temp = list(arr[j])
        for i in range(len(temp)):
            if i % 2 == 0:
                temp[i] = temp[i].upper()
            else:
                temp[i] = temp[i].lower()
        arr[j] = ''.join(temp)

    answer = ' '.join(arr)
    
    return answer

-----Others-----
def toWeirdCase(s):
    return " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
