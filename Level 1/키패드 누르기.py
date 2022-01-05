# https://programmers.co.kr/learn/courses/30/lessons/67256

-----Mine-----
def solution(numbers, hand):
    answer = ''
    
    nowHandLeft = '*'
    nowHandRight = '#'
    
    numDictForTwo = {1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, 0:3, '*':4, '#':4}
    numDictForFive = {1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, 0:2, '*':3, '#':3}
    numDictForEight = {1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, 0:1, '*':2, '#':2}
    numDictForZero = {1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, 0:0, '*':1, '#':1}
    
    for temp in numbers:
        if temp == 1 or temp == 4 or temp == 7:
            answer += 'L'
            nowHandLeft = temp
        elif temp == 3 or temp == 6 or temp == 9:
            answer += 'R'
            nowHandRight = temp
        elif temp == 2:
            if numDictForTwo.get(nowHandLeft) < numDictForTwo.get(nowHandRight):
                answer += 'L'
                nowHandLeft = temp
            elif numDictForTwo.get(nowHandLeft) > numDictForTwo.get(nowHandRight):
                answer += 'R'
                nowHandRight = temp
            else:
                if hand == 'left':
                    answer += 'L'
                    nowHandLeft = temp
                else:
                    answer += 'R'
                    nowHandRight = temp
        elif temp == 5:
            if numDictForFive.get(nowHandLeft) < numDictForFive.get(nowHandRight):
                answer += 'L'
                nowHandLeft = temp
            elif numDictForFive.get(nowHandLeft) > numDictForFive.get(nowHandRight):
                answer += 'R'
                nowHandRight = temp
            else:
                if hand == 'left':
                    answer += 'L'
                    nowHandLeft = temp
                else:
                    answer += 'R'
                    nowHandRight = temp
        elif temp == 8:
            if numDictForEight.get(nowHandLeft) < numDictForEight.get(nowHandRight):
                answer += 'L'
                nowHandLeft = temp
            elif numDictForEight.get(nowHandLeft) > numDictForEight.get(nowHandRight):
                answer += 'R'
                nowHandRight = temp
            else:
                if hand == 'left':
                    answer += 'L'
                    nowHandLeft = temp
                else:
                    answer += 'R'
                    nowHandRight = temp
        elif temp == 0:
            if numDictForZero.get(nowHandLeft) < numDictForZero.get(nowHandRight):
                answer += 'L'
                nowHandLeft = temp
            elif numDictForZero.get(nowHandLeft) > numDictForZero.get(nowHandRight):
                answer += 'R'
                nowHandRight = temp
            else:
                if hand == 'left':
                    answer += 'L'
                    nowHandLeft = temp
                else:
                    answer += 'R'
                    nowHandRight = temp
        
    return answer

-----Others-----
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
