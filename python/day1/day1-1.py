

f = open("input/input.txt", "r")

list1 = []
list2 = []

distance = 0
sim = 0

for line in f:
    entry = line.split("   ")
    list1.append(entry[0])
    list2.append(entry[1])

list1.sort()
list2.sort()

for i in range(len(list1)):
    if list1[i] > list2[i]:
        distance += int(list1[i]) - int(list2[i])
    elif list1[i] < list2[i]:
        distance += int(list2[i]) - int(list1[i])
    else:
        distance += 0


for i in range(len(list1)):
    # print("i=",list1[i])
    count = 0
    for j in range(len(list2)):
        # print('j=',list2[j])
        if int(list1[i]) == int(list2[j]):
            # print("count up!")
            count += 1
    sim += int(list1[i]) * count

print("distance =", distance)
print("similariy =", sim)
