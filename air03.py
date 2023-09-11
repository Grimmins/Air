import sys

def seekIntruder(list):
    for i in range(len(list)):
        if list.count(list[i]) == 1:
            return list[i]

if len(sys.argv) < 2:
    print("error")
    exit()
else:
    print(seekIntruder(sys.argv[1:]))