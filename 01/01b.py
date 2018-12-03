from d import *

freqset = set()

deltas = map(int, data.strip().split("\n"))

f = 0
i = 0
freqset.add(f)

#print(deltas)

while True:
    delta = deltas[i%len(deltas)]
    f += delta
    print("f is now", f)
    if f in freqset:
        print(f)
        break
    else:
        freqset.add(f)
        i += 1

