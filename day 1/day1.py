

f = open("input.txt", "r")
data = 0
sums = [-1, -1, -1]
fileIn = f.readline()


while fileIn:
    if fileIn.strip().isdigit():
        data += int(fileIn)
    else:
        newSum = data
        mini = min(sums)

        if newSum > mini:
            sums.remove(mini)
            sums.append(newSum)

        data = 0

    fileIn = f.readline()

#part 1
print(max(sums))

#part 2
print(sum(sums))
