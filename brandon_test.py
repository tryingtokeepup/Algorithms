import time


def move_zeros(a):
    counter = len(a) - 1
    while counter > -1:
        if a[counter] == 0:
            a += [a.pop(counter)]
        else:
            counter -= 1
    return a


start = time.time()
print(move_zeros([1, 0, 1, 1, 0, 1, 1, 1, 2, 0,
                  0, 0, 4, 5, 6, 8, 1, 12, 0, 45, 0, 3, 6]))
end = time.time()
print(end-start)
