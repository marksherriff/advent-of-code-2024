testing = True

if testing:
    f = open("input/testinput.txt", "r")
else:
    f = open("input.txt", "r")

for line in f:
    print(line)