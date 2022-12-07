f = open("input.txt", "r")

crates = [[],[],[],[],[],[],[],[],[]]
crates2 = [[],[],[],[],[],[],[],[],[]]

fileIn = f.readlines()


for i in range(7, -1, -1):
    line = fileIn[i]

    for j in range(1, 35, 4):
        crate = line[j:j+1].strip()
        if crate != " " and crate:
            crates[(j-1)//4].append(crate)
            crates2[(j-1)//4].append(crate)



for i in range(10, len(fileIn)):
    data = fileIn[i].split(" ")[1::2]

    controls = (int(data[0]), int(data[1])-1, int(data[2])-1)

    crates[controls[2]] += crates[controls[1]][-controls[0]:][::-1]
    crates[controls[1]] = crates[controls[1]][:-controls[0]]

    crates2[controls[2]] += crates2[controls[1]][-controls[0]:]
    crates2[controls[1]] = crates2[controls[1]][:-controls[0]]

print("Part 1: ")
for row in crates:
    print(row[-1], end="")

print("\nPart 2: ")

for row in crates2:
    print(row[-1], end="")