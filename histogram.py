import sys
import math

strings = []
ints = []
count = 0

for line in sys.stdin:
    x = line.split()
    for y in range(0,1):
        strings.append(x[0])
        ints.append(int(x[1]))
        count += int(x[1])

for x in range(0,len(strings)):
    print(strings[x], "[","*"*(2*ints[x]),"]", math.floor((ints[x]/count)*100), "%")

