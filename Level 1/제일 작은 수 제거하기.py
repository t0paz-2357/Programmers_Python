# https://programmers.co.kr/learn/courses/30/lessons/12935

-----Mine-----
def solution(arr):
    arr.remove(min(arr))
    
    if len(arr) == 0:
        return [-1]
    else:
        return arr

-----Others-----
def rm_small(mylist):
    return [i for i in mylist if i > min(mylist)]
