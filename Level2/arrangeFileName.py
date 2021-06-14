import re

def solution(files):
    # tmp = [re.split('[0-9]+', file) for file in files]
    # print(tmp)
    lst = [re.split('([0-9]+)', file) for file in files]
    # print(lst)
    lst.sort(key = lambda x : (x[0].lower(), int(x[1])))
    return [''.join(l) for l in lst]

print(solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))