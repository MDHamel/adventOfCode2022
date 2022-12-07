
f = open("./input.txt", "r")

# part 1
fileIn = f.readline().strip()
s = 0

while fileIn:
    data = (fileIn[:len(fileIn) // 2], fileIn[len(fileIn) // 2:])

    for item in data[0]:
        if item in data[1]:
            s += ord(item) - (96 if item.islower() else 38)
            break

    fileIn = f.readline().strip()


# part 2
f.seek(0)
fileIn = f.readlines()
s2 = 0

while fileIn:
    a = fileIn.pop(0).strip()
    b = fileIn.pop(0).strip()
    c = fileIn.pop(0).strip()

    shared = []

    for item in a:
        if item in b and item not in shared:
            shared.append(item)

    for item in shared:
        if item in c:
            s2 += ord(item) - (96 if item.islower() else 38)


print("Part One: {0}".format(s))
print("Part Two: {0}".format(s2))