import sys

def delString(tabString, string):
    return [i for i in tabString if string.lower() not in i and string.upper() not in i]

if len(sys.argv) < 2:
    print("error")
    exit()
else:
    [print(i, end=" ") for i in delString(sys.argv[1:-1], sys.argv[-1])]
    print('\n')