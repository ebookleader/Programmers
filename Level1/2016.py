import datetime
def solution(a, b):
    # week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    # d = datetime.datetime(2016, a, b)
    # answer = week[d.weekday()]
    # return answer
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return week[(sum(month[:a-1]) + (b-1)) % 7]

print(solution(1, 1))