f = open("input.txt", "r")
fileIn = f.readline().strip()
pt1Total = 0
pt2Total = 0

while fileIn:
    fileIn = fileIn.split(",")

    elf1 = list(map(int, fileIn[0].split("-")))
    elf2 = list(map(int, fileIn[1].split("-")))

    # part 1
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        pt1Total += 1

    # part 2
    if elf1[0] <= elf2[1] and elf2[0] <= elf1[1]:
        pt2Total += 1

    fileIn = f.readline().strip()

print(pt1Total)
print(pt2Total)