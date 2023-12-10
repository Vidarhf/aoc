
from os import environ
import pathlib
from functools import reduce
import collections
#find the tile in the loop that is farthest from the starting position
#find the tile that would take the longest number of steps along the loop to reach from the starting point - regardless of which way around the loop the animal went.
#How many steps along the loop does it take to get from the starting position to the point farthest from the starting position?

#140 char line length
#140 lines

#| is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
pipeDict = {'|': [[0, 1], [0, -1]], '-': [[1, 0], [-1, 0]], 'L': [[0, 1], [1, 0]], 'J': [[0,1], [-1,0]], '7': [[0, -1], [-1, 0]], 'F': [[0,-1], [1,0]]}
moveDict = {'up': ['|', '7', 'F'], 'down': ['L', '|', 'J'], 'left': ['-', 'L', 'F'], 'right': ['-', 'J', '7']}

# Function that returns all adjacent elements
def get_possible_moves(matrix, pos, size):
    possibleMoves = []
    # Define possible movements (up, down, left, right)
    movements = {'up': [0, -1], 'down': [0, 1], 'left': [-1, 0], 'right': [1, 0]}
    x = pos[0]
    y = pos[1]
    for move in movements.keys():
        new_x, new_y,  = x + movements[move][1], y + movements[move][0]
        # Check if the new position is within the matrix boundaries
        if 0 <= new_x < size and 0 <= new_y < size:
            #check that move is a matching pipe
            if matrix[new_x][new_y] in moveDict[move]:
                possibleMoves.append([new_x, new_y])
                

    return possibleMoves

def process_input(input_file):
    lines = pathlib.Path(input_file).read_text().strip().split('\n')
    size = len(lines)
    matrix = [['.' for _ in range(0, size)] for _ in range(0, size)]
    startPos = [0, 0]
    for r in range(0, size):
        line = lines[r]
        for c in range(0, size):
            char = line[c]
            if char == 'S':
                startPos[0], startPos[1] = r, c
            matrix[r][c] = char
    for row in matrix:
        print(row)

    #Start at startPos
    #Walk the pipe from different directions, when they meet we've found our furtherst point and number of steps
    startMoves = get_possible_moves(matrix, startPos, size)
    print('startmoves: ', startMoves)
    #Keep track of the path
    path = [startPos]
    steps = 0
    backAtPath = False
    walker = startPos
    while backAtPath != True:
        print("Walker: ", walker)
        moves = get_possible_moves(matrix, walker, size)
        print("Path: ", path)
        print("Possible moves: ", moves)
        for move in moves:
            if move == startPos:
                if walker[0] == startPos[0] and walker[1] == startPos[1 and steps > 1]:
                    print("Found our way back!")
                    print("Steps: ", steps)
                    backAtPath = True
                    break
            elif move not in path:
                print("Moving: ", move)
                walker[0] = move[0]
                walker[1] = move[1]
                path.append(move)
                steps += 1
                break
    # while a != b:

    print("Adjacent cells: ", get_possible_moves(matrix, startPos, size))
    print(startPos)
    return 0

#Extrapolate backwards
def process_input2(input_file):
    return 0

def getSolutionPart1(input_file):
    numOfSteps = process_input(input_file)
    return numOfSteps

def getSolutionPart2(input_file):
    numOfSteps = process_input2(input_file)
    return numOfSteps

#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))

if __name__ == '__main__':
    main('example.txt')