def high(x):
    def sum_word(a):
        return sum([ord(el)-96 for el in a])
    max1 = max([sum_word(i) for i in x.split()])
    s = [l for l in x.split() if sum_word(l) == max1]
    sorted(s, key=lambda y: s.index(y))
    return s[0]


print(high('man i need a taxi up to ubud'))  # , 'taxi')
print(high('what time are we climbing up the volcano'))   # , 'volcano')
print(high('take me to semynak'))  # , 'semynak')
print(high('aa b'))  # , 'aa')
print(high('b aa'))  # , 'b'))
print(high('bb d'))  # , 'bb')
print(high('d bb'))  # , 'd')
print(high("aaa b"))  # , "aaa")
print(ord('a'), ord('z'))