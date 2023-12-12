
from os import environ
import pathlib
from functools import reduce

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



def process_input(input_file):
    lines = [[x for x in l] for l in pathlib.Path(input_file).read_text().strip().split('\n')]
    size = len(lines)
    matrix = dict()
    startPos = ()
    for r in range(size):
        line = lines[r]
        for c in range(size):
            char = line[c]
            matrix[(r,c)] = char
            if char == 'S':
                startPos = (r,c)
    #0r,1down,2l,3up
    viableDirection = {0: ['7', '-', 'J'], 1: ['J', 'L', '|'], 2:['L', '-', 'F'], 3:['F', '7', '|']} 

    def move(p,d, matrix):
        R,C = p
        dc,dr = [1,0,-1,0],[0,1,0,-1]
        if matrix[p] == 'S' and d == 0: 
            for i in range(4):
                if (R+dr[i],C+dc[i]) in matrix:
                    if matrix[(R+dr[i],C+dc[i])] in viableDirection[i]:
                        return (R+dr[i],C+dc[i]),i
        elif matrix[p] == 'F' and d == 3: d = 0
        elif matrix[p] == 'F' and d == 2: d = 1

        elif matrix[p] == '7' and d == 0: d = 1
        elif matrix[p] == '7' and d == 3: d = 2

        elif matrix[p] == 'J' and d == 1: d = 2
        elif matrix[p] == 'J' and d == 0: d = 3

        elif matrix[p] == 'L' and d == 2: d = 3
        elif matrix[p] == 'L' and d == 1: d = 0
        return (R+dr[d],C+dc[d]),d

    #Start at startPos
    #Walk the pipe from different directions, when they meet we've found our furtherst point and number of steps
    #Keep track of the path
    path = set()
    backAtStart = True
    walker = startPos
    #starting direction
    direction =  0
    while backAtStart:
        walker, direction = move(walker, direction, matrix)
        if matrix[walker] == 'S':
            backAtStart = False
        if walker not in path:
            path.add(walker)
    furthestPos = len(path)//2 
    return furthestPos

#Extrapolate backwards
def process_input2(input_file):
    return 0

def getSolutionPart1(input_file):
    numberOfSteps = process_input(input_file)
    return numberOfSteps

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
    main('input.txt')