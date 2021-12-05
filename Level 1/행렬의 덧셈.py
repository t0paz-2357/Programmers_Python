# https://programmers.co.kr/learn/courses/30/lessons/12950

-----Mine-----
import numpy as np

def solution(arr1, arr2):
    return (np.array(arr1) + np.array(arr2)).tolist()

-----Others-----
def sumMatrix(A,B):
    answer = [[c + d for c, d in zip(a, b)] for a, b in zip(A,B)]
    return answer
