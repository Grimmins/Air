import sys

def concat(tabCh, sep):
    ch = ""
    for i in range(len(tabCh)):
        ch += tabCh[i]
        if i < len(tabCh) - 1:
            ch += sep
    return ch

if len(sys.argv) < 2:
    print("error")
    exit()
else:
    print(concat(sys.argv[1:-1], sys.argv[-1]))










