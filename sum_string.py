def sum_strings(x, y):
    x = x.lstrip('0')
    if not x: x = '0'
    y = y.lstrip('0')
    if not y: y = '0'
    max_l = max(len(x), len(y))
    x = '0' * (max_l - len(x)) + x
    y = '0' * (max_l - len(y)) + y
    x = [int(i) for i in list(x)]
    y = [int(j) for j in list(y)]
    for i in range(max_l):
        x[i] += y[i]
    print(x)
    while [1 for i in x[1:] if i > 9]:
        for i in range(-1, -len(x), -1):
            if x[i] > 9:
                x[i] %= 10
                x[i-1] += 1
        print(x)
    return ''.join([str(i) for i in x]) if x else '0'


print(sum_strings('456', '999'*100))
