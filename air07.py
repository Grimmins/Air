import sys

def keepSorted(tabNumbers, number):
    for i in tabNumbers:
        if i > number:
            tabNumbers.insert(tabNumbers.index(i), number)
            return tabNumbers

if len(sys.argv) < 3:
    print("error")
    exit()
else:
    [print(i, end=" ") for i in keepSorted(sys.argv[1:-1], sys.argv[-1])]
    print('\n')
