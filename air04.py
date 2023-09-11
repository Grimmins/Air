import sys

def delRepeat(string):
    newString = string[0]
    for i in range(1,len(string)):
        if string[i] != newString[-1]:
            newString += string[i]
    return newString

if len(sys.argv) != 2:
    print("error")
    exit()
else:
    print(delRepeat(sys.argv[1]))