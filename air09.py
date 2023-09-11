import sys

def rotLeft(a):
    return a[1:] + a[:1]

if len(sys.argv) < 3:
    print("error")
    exit()
else:
    [print(i, end=" ") for i in rotLeft(sys.argv[1:])]
    print('\n')
