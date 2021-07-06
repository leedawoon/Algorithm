def solution(x):
    n = sum(map(int, str(x)))
    res = x / n
    return res.is_integer()

print(solution(13))