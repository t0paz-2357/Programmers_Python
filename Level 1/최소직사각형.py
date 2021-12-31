# https://programmers.co.kr/learn/courses/30/lessons/86491

-----Mine-----
def solution(sizes):
    maxW = maxH = 0
    
    for temp in sizes:
        if temp[0] < temp[1]:
            tmp = temp[1]
            temp[1] = temp[0]
            temp[0] = tmp
            
    for temp in sizes:
        if maxW < temp[0]:
            maxW = temp[0]
        if maxH < temp[1]:
            maxH = temp[1]

    return maxW * maxH

-----Others-----
solution = lambda sizes: max(sum(sizes, [])) * max(min(size) for size in sizes)
