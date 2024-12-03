import re

TESTING = False
SUM_TOTAL = 0
DO_DONT = True

### MAIN
if TESTING:
    f = open("input/testinput.txt", "r")
else:
    f = open("input/input.txt", "r")

## The instructions never specified if we should treat a new line as starting as active or not.
## So this is a failure in the requirements. :-)
active = True
for line in f:
    results = re.findall("mul[(][0-9]+[,][0-9]+[)]|don't[(][)]|do[(][)]", line)
    print(results)
   # active = True
    for result in results:
        print(result)
        if result == "don't()":
            print("inactive")
            active = False
        elif result == "do()":
            print("active")
            active = True
        elif active:
            print("math time!")
            num = result.split(",")
            num_1 = num[0][4:]
            num_2 = num[1][:len(num[1])-1]
            print(num_1, num_2)
            SUM_TOTAL += int(num_1) * int(num_2)

print(SUM_TOTAL)