import sys

def operation(list, operation):
    if operation[0] == "+":
        return [int(i) + int(operation[1:]) for i in list]
    elif operation[0] == "-":
        return [int(i) - int(operation[1:]) for i in list]
    else:
        return list

if len(sys.argv) < 3 or sys.argv[-1][0] not in "+-" or not sys.argv[-1][1:].isdigit():
    print("error")
    exit()
else:
    [print(i, end=" ") for i in operation(sys.argv[1:-1], sys.argv[-1])]
    print('\n')