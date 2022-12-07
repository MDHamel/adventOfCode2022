f = open("input.txt", "r")
fileIn = f.readline()

pt1total = 0
pt1 = {
    "A X": 4,   #draw
    "A Y": 8,   #win
    "A Z": 3,   #lose
    "B X": 1,   #lose
    "B Y": 5,   #draw
    "B Z": 9,   #win
    "C X": 7,   #win
    "C Y": 2,   #lose
    "C Z": 6    #draw
}


pt2total = 0
options = ("rock", "paper", "scissors")
cheating = {
    "X": 1,     #lose
    "Y": 0,     #draw
    "Z": 2,     #win
}
points = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
    "X": 0,
    "Y": 3,
    "Z": 6
}


while fileIn:
    #steps were simple enough to plot out into a map, making the overall runtime O(n)
    pt1total += pt1[fileIn.strip()]

    '''
    step 1) Split up input from other elf's choice (fileIn[0]) and your choice to win, lose, or draw (fileIn[1])
    step 2) Subtract 65 from the integer value of the character so that we can get the index of the other elf's choice
            from the options tuple
    step 3) Subtract from step 2's value to discern your choice and get the point value (winning values are to the right
            and losing values are to the left of the index. i.e. if the other elf chooses paper, we can win by 
            subtracting 2 equaling index -1 which is scissors or lose by subtracting 1 and getting rock at index 0;
    step 4) Add the point value of the win, lose, or draw
    '''
    fileIn = fileIn.strip().split(" ")
    pt2total += points[options[ord(fileIn[0]) - 65 - cheating[fileIn[1]]]] + points[fileIn[1]]

    fileIn = f.readline()


print(pt1total)
print(pt2total)
