import sys

def pyramide(char, size):
    if size < 1:
        return ""
    result = ""
    for i in range(1, size + 1):
        result += " " * (size - i) * 2  # Ajoute des espaces pour décaler le contenu vers la droite
        result += (char + " ") * (2 * i - 1)  # Utilise (char + " ") pour séparer les caractères par des espaces
        result += "\n"
    return result

if len(sys.argv) != 3 or len(sys.argv[1]) != 1 or not sys.argv[2].isdigit():
    print("error")
    exit()
else:
    print(pyramide(sys.argv[1], int(sys.argv[2])))
    print('\n')