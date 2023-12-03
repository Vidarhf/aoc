
from os import environ

COLUMNS = 140
ROWS = 140
 
# Function that returns all adjacent elements
def get_adjacent_cells(matrix, row, col):
    rows = ROWS
    cols = COLUMNS
    adjacent_cells = {}

    # Define possible movements (up, down, left, right, diagonals)
    movements = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dr, dc in movements:
        new_row, new_col = row + dr, col + dc

        # Check if the new position is within the matrix boundaries
        if 0 <= new_row < rows and 0 <= new_col < cols:
            adjacent_cells[new_col, new_row] = matrix[new_row, new_col]

    return adjacent_cells


def build_matrix(input_file):
    #Create a dictionary to hold the matrix
    matrix = {}
    with open(input_file, "r") as f:
        y = 0
        for line in f:
            for i in range(0, COLUMNS):
                #Assign the value to the matrix
                matrix[i,y] = line[i]
            y += 1  
    return matrix

def buildNumber(matrix, i, j):
    #Get the digits on the left and right of the symbol
    #Add them together to one number
    #Return the number
    number = str(matrix[i, j])
    checkedTuples = []
    for rightIterator in range(1, 10):
        if(i+rightIterator >= COLUMNS):
            break
        if matrix[i+rightIterator, j].isdigit():
            number += str(matrix[i+rightIterator, j])
            checkedTuples.append((i+rightIterator, j))
        else:
            break
    for leftIterator in range(1, 10):
        if(i-leftIterator < 0):
            break
        if matrix[i-leftIterator, j].isdigit():
            number = str(matrix[i-leftIterator, j]) + number
            checkedTuples.append((i-leftIterator, j))
        else:
            break
    return [number, checkedTuples]

def buildNumber2(matrix, i, j):
    #Get the digits on the left and right of the symbol
    #Add them together to one number
    #Return the number
    number = str(matrix[i, j])
    checkedTuples = []
    for rightIterator in range(1, 10):
        if(i+rightIterator >= COLUMNS):
            break
        if matrix[i+rightIterator, j].isdigit():
            number += str(matrix[i+rightIterator, j])
            checkedTuples.append((i+rightIterator, j))
        else:
            break
    for leftIterator in range(1, 10):
        if(i-leftIterator < 0):
            break
        if matrix[i-leftIterator, j].isdigit():
            number = str(matrix[i-leftIterator, j]) + number
            checkedTuples.append((i-leftIterator, j))
        else:
            break
    return [number, checkedTuples]

def getSumFromNeighbours(neighbours, matrix):
    total = 0
    checked = {}
    for neighbour in neighbours.keys():
        alreadyChecked = checked.get(neighbour)
        if alreadyChecked:
            continue
        value = neighbours[neighbour]
        # Find the adjacent numbers and build a list of them
        if value.isdigit():
            numberAndNeighbours = buildNumber(matrix, neighbour[1], neighbour[0]) #flipped because of the way the matrix is built
            for tuple in numberAndNeighbours[1]:
                checked[tuple[1], tuple[0]] = True #flipped because of the way the matrix is built
            total += int(numberAndNeighbours[0])
    return total

def getGearRatio(neighbours, matrix):
    total = 1
    checked = {}
    numOfAdjacentNumbers = 0
    for neighbour in neighbours.keys():
        alreadyChecked = checked.get(neighbour)
        if alreadyChecked:
            continue
        value = neighbours[neighbour]
        # Find the adjacent numbers and build a list of them
        if value.isdigit():
            numberAndNeighbours = buildNumber(matrix, neighbour[1], neighbour[0]) #flipped because of the way the matrix is built
            for tuple in numberAndNeighbours[1]:
                checked[tuple[1], tuple[0]] = True #flipped because of the way the matrix is built
            numOfAdjacentNumbers += 1
            if numOfAdjacentNumbers > 2:
                return 0
            total = total * int(numberAndNeighbours[0])
    if numOfAdjacentNumbers != 2:
        return 0
    return total


def findSum(matrix):
    #Find the symbols in the matrix
    total = 0
    for i in range(0, COLUMNS):
        for j in range(0, ROWS):
            value = matrix[i,j]
            #If we find a symbol other than a digit or a dot
            if value != '.' and value.isdigit() == False:
                # Find the adjacent numbers
                neighbours = get_adjacent_cells(matrix, i, j)
                #For each adjacent number, add it to the total
                total += getSumFromNeighbours(neighbours, matrix)

                # total += find_closest_numbers(matrix, i, j)
    #Return the sum of the adjacent numbers
    return total

def findSum2(matrix):
    #Find the symbols in the matrix
    total = 0
    for i in range(0, COLUMNS):
        for j in range(0, ROWS):
            value = matrix[i,j]
            #If we find a symbol other than a digit or a dot
            if value == '*':
                # Find the adjacent numbers
                neighbours = get_adjacent_cells(matrix, i, j)
                #For each adjacent number, add it to the total
                total += getGearRatio(neighbours, matrix)
    #Return the sum of the adjacent numbers
    return total

def getSolutionPart1(input_file):
    total = 0
    #Build our matrix
    matrix = build_matrix(input_file)
    #Find symbols in the matrix and return the sum of adjacent numbers
    total = findSum(matrix)
    # total += process_line(line)
    return total

def getSolutionPart2(input_file):
    total = 0
    #Build our matrix
    matrix = build_matrix(input_file)
    #Find gear ratio
    total = findSum2(matrix)
    # total += process_line(line)
    return total

#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))
    

main('input.txt')