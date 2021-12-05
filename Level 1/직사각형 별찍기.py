# https://programmers.co.kr/learn/courses/30/lessons/12969

-----Mine-----
a, b = map(int, input().strip().split(' '))
for i in range(b):
    for j in range(a):
        print('*', end='')
    print()

-----Others-----
a, b = map(int, input().strip().split(' '))
answer = ('*'*a +'\n')*b
print(answer)
