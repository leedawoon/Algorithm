def solution(s):
    med = len(s) // 2
    res = (lambda s: s[(med-1):(med+1)] if len(s) % 2 == 0 else s[med])(s)
    return res

print(solution('power'))