import sys

def split(ch, sep):
    sh = ""
    tabCh = []
    for i in range(len(ch)):
        if ch[i] == sep:
            tabCh.append(sh)
            sh= ""
        elif i == len(ch)-1:
            sh += ch[i]
            tabCh.append(sh)
        else:
            sh += ch[i]
    return tabCh

if len(sys.argv) != 2:
    print("error")
    exit()
else:
    [print(i) for i in split(sys.argv[1], " ")]