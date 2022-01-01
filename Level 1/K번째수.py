# https://programmers.co.kr/learn/courses/30/lessons/42748

-----Mine-----
def solution(array, commands):
    answer = []
    
    for temp in commands:
        tempArr = []
        for i in range(temp[0] - 1, temp[1]):
            tempArr.append(array[i])
        tempArr.sort()
        answer.append(tempArr[temp[2] - 1])
        
    return answer

-----Others-----
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
