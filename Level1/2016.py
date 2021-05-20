import datetime
def solution(a, b):
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    d = datetime.datetime(2016, a, b)
    answer = week[d.weekday()]
    return answer

print(solution(2, 29))