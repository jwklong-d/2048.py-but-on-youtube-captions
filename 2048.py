import random

#return 1 EMPTY, RANDOM positions to put a value

# def getPosition(grid):
#     result = dict()
#     result["row"] = random.randint(0,3)
#     result["column"] = random.randint(0,3)
#     if grid[result["row"]][result["column"]]==0:
#         return result
#     else:
#         return getPosition(grid)
def getPosition(grid):
    possibleVacancies = []
    for i in range(0,4):
        for j in range(0,4):
            if(grid[i][j] == 0):
                result = dict()
                result["row"] = i
                result["column"] = j
                possibleVacancies.append(result)
    return possibleVacancies[random.randint(0, len(possibleVacancies)-1)]

def insertValue(grid):
    startPosition = getPosition(grid)
    grid[startPosition["row"]][startPosition["column"]] = 2 if random.randint(0, 100) % 2 == 0 else 4

def startGame(grid):
    for x in range(2):
        insertValue(grid)

def display(grid):
    for row in grid:
        print(row)
    print("============")

def reverse(row):
    temp = []
    for i in range(3, -1, -1):
        temp.append(row[i])
    return temp

def mergeLeftPos(row):
    newRow = [0,0,0,0]
    newRowIndex = 0
    for i in row:
        if i != 0:
            newRow[newRowIndex] = i
            newRowIndex+=1
    return newRow
def mergeLeftCalc(row):
    for i in range(0,3):
        if row[i]!=0:
            if row[i] == row[i+1]:
                row[i]*=2
                row[i+1]=0
                mergeLeftPos(row)
    return mergeLeftPos(row)
def mergeLeft(row):
    return mergeLeftCalc(mergeLeftPos(row))

def mergeLeftBoard(grid):
    temp = []
    for row in grid:
        row = mergeLeft(row)
        temp.append(row)
    return temp

def mergeRightBoard(grid):
    temp = []
    for row in grid:
        tempRow = reverse(row)
        tempRow = mergeLeft(tempRow)
        tempRow = reverse(tempRow)
        temp.append(tempRow)
    return temp

def mergeUp(grid):
    temp = transpose(grid)
    temp = mergeLeftBoard(temp)
    temp = transpose(temp)

    return temp


def mergeDown(grid):
    temp = transpose(grid)
    temp = mergeRightBoard(temp)
    temp = transpose(temp)

    return temp

def transpose(grid):
    transpose = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for column in range(0,4):
        for row in range(0, 4):
            transpose[row][column] = grid[column][row]
    return transpose

def keepPlaying(grid):
    for row in grid:
        if 2048 in row:
            print("Well done you've won the game")
            return False
        if 0 in row:
            return True
    # all filled and no 2048
    print("Game lost")
    return False

if __name__ == '__main__':
    # grid = [
    #     [1024,0,0,0],
    #     [1024,0,0,0],
    #     [0,0,0,0],
    #     [0,0,0,0]
    # ]
    grid = [
        [2,2,2,0],
        [4,4,4,0],
        [8,8,8,8],
        [16,16,16,0]
    ]
    display(grid)
    startGame(grid)
    display(grid)
    while(keepPlaying(grid)):
        merge = input("which way?")
        if merge == "d":
            grid = mergeRightBoard(grid)
            insertValue(grid)
            display(grid)
        elif merge =="w":
            grid = mergeUp(grid)
            insertValue(grid)
            display(grid)
        elif merge == "s":
            grid = mergeDown(grid)
            insertValue(grid)
            display(grid)
        elif merge == "a":
            grid = mergeLeftBoard(grid)
            insertValue(grid)
            display(grid)

    # grid[0] = mergeLeft(grid[0])
    # grid = mergeLeftBoard(grid)
    # display(grid)
    # grid = mergeRightBoard(grid)
    # display(grid)
    # grid = mergeUp(grid)
    # display(grid)
    # grid = mergeDown(grid)
    # display(grid)

    # trasposeTest = [
    #     [1,2,3,4],
    #     [5,6,7,8],
    #     [9,10,11,12],
    #     [13,14,15,16]
    # ]
    # display(trasposeTest)
    # display(transpose(trasposeTest))
