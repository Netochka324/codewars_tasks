def oper(a, *inn):
    if inn[0][1] == '+':
        return a+inn[0][0]
    if inn[0][1] == '-':
        return a-inn[0][0]
    if inn[0][1] == '*':
        return a*inn[0][0]
    if inn[0][1] == '/':
        if a != 0:
            return int(a/inn[0][0])
        return 'division by zero'


def zero(*inn):  # your code here
    if inn:
        return oper(0, *inn)
    else:
        return 0


def one(*inn):  # your code here
    if inn:
        return oper(1, *inn)
    else:
        return 1


def two(*inn):  # your code here
    if inn:
        return oper(2, *inn)
    else:
        return 2


def three(*inn):  # your code here
    if inn:
        return oper(3, *inn)
    else:
        return 3


def four(*inn):  # your code here
    if inn:
        return oper(4, *inn)
    else:
        return 4


def five(*inn):  # your code here
    if inn:
        return oper(5, *inn)
    else:
        return 5


def six(*inn):  # your code here
    if inn:
        return oper(6, *inn)
    else:
        return 6


def seven(*inn):  # your code here
    if inn:
        return oper(7, *inn)
    else:
        return 7


def eight(*inn):  # your code here
    if inn:
        return oper(8, *inn)
    else:
        return 8


def nine(*inn):  # your code here
    if inn:
        return oper(9, *inn)
    else:
        return 9


def plus(*inn):  # your code here
    return *inn, '+'


def minus(*inn):  # your code here
    return *inn, '-'


def times(*inn):  # your code here
    return *inn, '*'


def divided_by(*inn):  # your code here
    return *inn, '/'


print(seven(times(five())), 35)
print(four(plus(nine())), 13)
print(eight(minus(three())), 5)
print(six(divided_by(two())), 3)
