from d import *

def has(s, n):
    dc = {}
    for char in s:
        if char not in dc:
            dc[char] = 1
        else:
            dc[char] += 1

    return n in dc.values()

def sumHas(ss, n):
    num = 0
    for s in ss:
        if has(s, n):
            num += 1
    return num

def solve():
    ss = data.strip().split()

    print(sumHas(ss, 2) * sumHas(ss, 3))

solve()
