def partialSums(*k):
    a = [0]
    d = 0
    for i in k:
        d += i
        a.append(d)
    return a


print(partialSums(1, 0.5, 0.25, 0.125))
