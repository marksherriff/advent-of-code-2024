import re

TESTING = True
SUM_TOTAL = 0
DO_DONT = True

### MAIN
if TESTING:
    f = open("input/testinput.txt", "r")
else:
    f = open("input/input.txt", "r")

for line in f:
    results = re.findall("mul[(][0-9]+[,][0-9]+[)]", line)
    print(results)
    for result in results:
        num = result.split(",")
        num_1 = num[0][4:]
        num_2 = num[1][:len(num[1])-1]
        SUM_TOTAL += int(num_1) * int(num_2)

print(SUM_TOTAL)