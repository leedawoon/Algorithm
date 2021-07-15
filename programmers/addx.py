def solution(x, n):
    lst = []
    for i in range(n):
        lst.append(x * (i+1))     
    return lst

print(solution(2, 5))