import sys


def quick_sort(list):
    if len(list) <= 1:
        return list
    pivot = list[0]
    left = []
    right = []
    for x in list[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quick_sort(left) + [pivot] + quick_sort(right)

if len(sys.argv) < 2:
    print("error")
    exit()
else:
    [print(i, end=" ") for i in quick_sort(sys.argv[1:])]
    print('\n')