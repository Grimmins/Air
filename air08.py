import sys

def keepSorted(tabNumbers, number):
    for i in tabNumbers:
        if tabNumbers[-1] < number:
            tabNumbers.append(number)
            return tabNumbers
        elif i > number:
            tabNumbers.insert(tabNumbers.index(i), number)
            return tabNumbers

def fusion(tab1, tab2):
    for i in tab2:
        tab1 = keepSorted(tab1, i)
    return tab1


def getFirstTab():
    tab = []
    for i in sys.argv[1:]:
        if i == "fusion":
            return tab
        else:
            tab.append(int(i))
    return tab

def getSecondTab():
    return [int(i) for i in sys.argv[sys.argv.index("fusion")+1:]]

if len(sys.argv) < 4 or "fusion" not in sys.argv:
    print("error")
    exit()
else:
    [print(i, end=" ") for i in fusion(getFirstTab(), getSecondTab())]
    print('\n')


