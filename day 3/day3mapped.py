
f = open("input.txt", "r")

times = []


# part 1
fileIn = f.readline().strip()
s = 0

while fileIn:
    data = (fileIn[:len(fileIn) // 2], fileIn[len(fileIn) // 2:])
    m = {}
    for item in data[0]:
        m[item] = True

    for item in data[1]:
        if m.get(item):
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

    m = {}
    shared = {}

    for item in a:
        m[item] = True

    for item in b:
        if m.get(item) and not shared.get(item):
            shared[item] = True

    for item in c:
        if shared.get(item):
            s2 += ord(item) - (96 if item.islower() else 38)
            break


print("Part One: {0}".format(s))
print("Part Two: {0}".format(s2))

