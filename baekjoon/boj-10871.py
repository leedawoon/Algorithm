n, x = map(int, input().split(' '))
a = input().split(' ')

lst = []
for i in a:
    if int(i) < x:
        lst.append(i)
print(' '.join(lst))
