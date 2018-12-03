from d import *

data = data.strip().split()

def comp(s1, s2):
    s = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            s += s1[i]
    return s

def solve():
    for i in data:
        for j in data:
            if len(i) - len(comp(i,j)) == 1:
                print(comp(i,j))

solve()
