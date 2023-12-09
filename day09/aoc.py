
from os import environ
import pathlib
from functools import reduce
import collections

#Predict the next value in each history
#Make a new sequence from the difference at each step of the history
#If that sequence is not all zeroes, repeat, using the sequence just generated as the new history
#Once all of the valeus in the latest squeance are zeroes, extrapolate what the next valuye of teh original history should be
#To extrapolate: start by adding a new zero to the end of the list with zeroes, add placeholders on the every sequence above it
# The placeholder is the result of increasing the value to its left by the value below it. In our example input, 0, 3(0+3), 18 (15+3)
# Find the next value in each history and add them together. What is the sum of these extrapolated values?

def process_input(input_file):
    lines = pathlib.Path(input_file).read_text().strip().split('\n')
    sequences = []
    for line in lines:
        numbers = [int(num) for num in line.split(' ')]
        sequences.append(numbers)
    sumOfSequences = 0
    #Make a new sequence from the difference at each step of the history
    for sequence in sequences:
        history = sequence
        lastNumbers = [history[-1]]
        #If that sequence is not all zeroes, repeat, using the sequence just generated as the new history
        while True:
            newHistory = []
            for i in range(0, len(history)-1):
                newNum = history[i+1] - history[i]
                newHistory.append(newNum)
            if(len(history) == 1):
                newHistory.append(history[0])
                lastNumbers.append(history[0])
            if(len(history) > 1):
                lastNumbers.append(newHistory[-1])
            if all(value == 0 for value in newHistory) or len(newHistory) == 1:
                break
            history = newHistory
        lastNumbers.reverse()
        addedSequenceNumbers = [0 for i in lastNumbers]
        for i in range(0, len(lastNumbers)):
            addedSequenceNumbers[i] = lastNumbers[i] + addedSequenceNumbers[i-1]
        sumOfSequences += addedSequenceNumbers[-1]
    return sumOfSequences

#Extrapolate backwards
def process_input2(input_file):
    lines = pathlib.Path(input_file).read_text().strip().split('\n')
    sequences = []
    for line in lines:
        numbers = [int(num) for num in line.split(' ')]
        sequences.append(numbers)
    sumOfSequences = 0
    #Make a new sequence from the difference at each step of the history
    for sequence in sequences:
        history = collections.deque(sequence)
        firstNumbers = collections.deque([history[0]])
        while True:
            newHistory = []
            for i in range(0, len(history)-1):
                newNum = history[i+1] - history[i]
                newHistory.append(newNum)
            if(len(history) == 1):
                newHistory.append(history[0])
                firstNumbers.append(history[0])
            if(len(history) > 1):
                firstNumbers.appendleft(newHistory[0])
            if all(value == 0 for value in newHistory) or len(newHistory) == 1:
                break
            history = newHistory
        addedNumbers = [0 for i in firstNumbers]
        for i in range(0, len(firstNumbers)):
            addedNumbers[i] =  firstNumbers[i] - addedNumbers[i-1]
        sumOfSequences += addedNumbers[-1]
    return sumOfSequences

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