# https://programmers.co.kr/learn/courses/30/lessons/42840

-----Mine-----
def solution(answers):
    answer = [0, 0, 0]

    oneAnswer = [1,2,3,4,5] * 2000
    twoAnswer = [2,1,2,3,2,4,2,5] * 1250
    threeAnswer = [3,3,1,1,2,2,4,4,5,5] * 1000
    correctNum = []
    
    for i in range(len(answers)):
        if answers[i] == oneAnswer[i]:
            answer[0] += 1
        if answers[i] == twoAnswer[i]:
            answer[1] += 1
        if answers[i] == threeAnswer[i]:
            answer[2] += 1

    m = max(answer)
    
    for i in range(len(answer)):
        if m == answer[i]:
            correctNum.append(i + 1)
    
    correctNum.sort()
    
    return correctNum

-----Others-----
def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0, 0, 0]
    result = []

    for idx, answer in enumerate(answers):
        if answer == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if answer == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if answer == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)

    return result
