from os import system
import os
import sys

if len(sys.argv) < 2 or not os.path.isfile(sys.argv[1]):
    print("error")
else:
    system("cat " + sys.argv[1])
    print('\n')
exit()