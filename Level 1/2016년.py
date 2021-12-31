# https://programmers.co.kr/learn/courses/30/lessons/12901

-----Mine-----
import datetime

def solution(a, b):
    day = {0: 'MON', 1: 'TUE', 2: 'WED', 3: 'THU', 4: 'FRI', 5: 'SAT', 6: 'SUN'}
    
    return day[datetime.date(2016, a, b).weekday()]

-----Others-----
import datetime

def getDayName(a,b):
    t = 'MON TUE WED THU FRI SAT SUN'.split()
    return t[datetime.datetime(2016, a, b).weekday()]
