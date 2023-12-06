
from os import environ
import pathlib
import re
from functools import reduce
import numpy

# input example
# Time:      7  15   30
# Distance:  9  40  200

def process_input(input_file):
    input = pathlib.Path(input_file).read_text().split('\n')
    times = input[0].split()[1:]
    distances = input[1].split()[1:]

    return times, distances
def getNumberOfWaysToBeatRecord(times, distances):
    numberOfWaysToBeatRecord = [0 for x in times]

    #For each milisecond waited, we travel one milimeter longer per second
    for i in range(0, times.__len__()):
        time = int(times[i])
        record = int(distances[i])
        #We dont need to check j 0 or time length sich that result is distance = 0
        for j in range(1, time):
            attempt = j * (time-j)
            if attempt > record:
                numberOfWaysToBeatRecord[i] += 1
        i += 1
    # Multiply each element in the array
    # Example array
    return reduce(lambda x, y: x * y, numberOfWaysToBeatRecord)

def getNumberOfWaysToBeatRecord2(time, distance):
    numberOfWaysToBeatRecord = 0
    #For each milisecond waited, we travel one milimeter longer per second
    #We dont need to check j 0 or time length sich that result is distance = 0
    for j in range(1, time):
        attempt = j * (time-j)
        if attempt > distance:
            numberOfWaysToBeatRecord += 1
    # Multiply each element in the array
    # Example array
    return numberOfWaysToBeatRecord
#Determine number of ways you can beat the record in each race
def getSolutionPart1(input_file):
    times, distances = process_input(input_file)
    return getNumberOfWaysToBeatRecord(times, distances)

def getSolutionPart2(input_file):
    times, distances = process_input(input_file)
    #Multiply each element in the array
    time = int("".join(times))
    distance =int("".join(distances))
    return getNumberOfWaysToBeatRecord2(time, distance)


#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))
    

    
if __name__ == '__main__':
    main('input.txt')