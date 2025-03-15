def matrix(*arg):
    if len(arg) == 1:
        return [[0] * arg[0] for i in range(arg[0])]
    elif len(arg) == 0:
        return [[0]]
    elif len(arg) == 2:
        return [[0] * arg[1] for i in range(arg[0])]
    elif len(arg) == 3:
        return [[arg[2]] * arg[1] for i in range(arg[0])]


rows = matrix(2)
for row in rows:
    print(*row)
