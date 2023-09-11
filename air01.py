import sys


def split(ch, sep):
    tabCh = []
    i = 0
    while i < len(ch):
        if ch[i:i+len(sep)] == sep:
            tabCh.append(ch[:i])
            ch = ch[i+len(sep):]
            i = 0
        else:
            i += 1
    tabCh.append(ch)
    return tabCh


if len(sys.argv) != 2:
    print("error")
    exit()
else:
    [print(i) for i in split(sys.argv[1], "les")]
