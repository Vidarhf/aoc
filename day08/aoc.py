
import math
from os import environ
import pathlib
from functools import reduce
dirs = {'L': 0, 'R': 1}

def process_input(input_file):
    input = pathlib.Path(input_file).read_text().split('\n')
    lrInstructions = [dirs[lr] for lr in input[0]]
    lookUpTable = {}
    for line in input[2:]:
        key, lr = line.split('=')
        key = key.strip()
        lr = lr.replace('(', "").replace(')', "").replace(' ', "")
        lr = tuple(lr.split(','))
        lookUpTable.update({key: lr})
    numOfSteps = 0
    nextNode = 'AAA'  
    while numOfSteps < 100000:
        nextNode = lookUpTable[nextNode][lrInstructions[numOfSteps % len(lrInstructions)]]
        numOfSteps += 1
        if nextNode == 'ZZZ':
            break
    return numOfSteps

def process_input2(input_file):
    input = pathlib.Path(input_file).read_text().split('\n')
    lrInstructions = [dirs[lr] for lr in input[0]]
    lookUpTable = {}
    startingNodes = {}
    for line in input[2:]:
        key, lr = line.split('=')
        key = key.strip()
        lr = lr.replace('(', "").replace(')', "").replace(' ', "")
        lr = tuple(lr.split(','))
        lookUpTable.update({key: lr})
        if key[2] == 'A':
            startingNodes.update({key: key})
    foundEndSteps = []
    for nodeKey in startingNodes.keys():
        currentNode = startingNodes[nodeKey]
        count = 0
        while not currentNode.endswith('Z'):
            currentNode = lookUpTable[currentNode][lrInstructions[count % len(lrInstructions)]]
            count += 1
        foundEndSteps.append(count)
    return math.lcm(*foundEndSteps)

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
    main('input.txt')