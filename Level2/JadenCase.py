def solution(s):
    res = []
    s = s.split(' ')
    for word in s:
        if word == '':
            res.append(word)
        elif word[0].isalpha():
            capital = word[0].upper()
            word = capital + word[1:].lower()
            res.append(word)
        elif word[0].isdigit():
            res.append(word.lower())

    return ' '.join(res)

print(solution('for   the last week'))