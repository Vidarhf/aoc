
from os import environ
import pathlib
import re

def get_seeds(almanac):
    # Find the seeds
    seeds = [int(seed) for seed in almanac[0].split(':')[1].split()]
    return(seeds)

def find_lowest_location_within_seeds(almanac):
    seedList = get_seeds(almanac[0])
    seedPairs = [[seedList[i], seedList[i] + seedList[i+1]-1] for i in range(0, len(seedList), 2)]
    maps = almanac[1:]
    #Remove map names
    maps = [x[1:] for x in maps]
    for map in maps:
        i = 0
        while i < len(seedPairs):
            found = False
            seedStart, seedEnd = seedPairs[i]
            for line in map:
                destination, source, rangeLength = [int(x) for x in line.split()]
                if seedStart >= source and seedStart < (source + rangeLength) and found == False:
                    found = True
                    seedPairs[i][0] = destination + (seedStart - source)
                    if seedEnd < source + rangeLength:
                        seedPairs[i][1] = destination + (seedEnd - source)
                    else:
                        seedPairs[i][1] = destination + rangeLength - 1
                        seedPairs.append([source + rangeLength, seedEnd])

                elif seedEnd >= source and seedEnd < (source + rangeLength) and found == False:
                    found = True
                    seedPairs[i][1] = destination + (seedEnd - source)
                    if seedStart > source:
                        seedPairs[i][0] = destination + (seedStart - source)
                    else:
                        seedPairs[i][0] = destination
                        seedPairs.append([seedStart, source-1])
            i += 1
    return min(min(s) for s in seedPairs)    

def findLowestLocation(almanacMaps, seeds):
    locations = []
    for seed in seeds:
            lastDestination = int(seed)
            for mapIndex in range(0, almanacMaps.__len__()):
                map = almanacMaps[mapIndex]
                #For each line
                for line in map:
                    if(line == ""):
                        continue
                    #Split the line
                    lineSplit = line.split(" ")
                    #Get the destination range
                    destinationRangeStart = int(lineSplit[0])
                    #Get the source range start
                    sourceRangeStart = int(lineSplit[1])
                    #Get the range length
                    rangeLength = int(lineSplit[2])
                    #Lookup source number conversion or stay at same value
                    #Within source range
                    if (sourceRangeStart <= lastDestination <= sourceRangeStart + rangeLength):           
                        lastDestination = (lastDestination - sourceRangeStart) + destinationRangeStart
                        break                 
            locations.append(lastDestination)
    #Find lowest location and strip decimals
    lowestLocation = str(min(locations))
    return(int(lowestLocation))

def process_almanac(almanac):
    #split the almanac into conversion categories
    #Get seeds
    seeds = get_seeds(almanac[0])
    #Remove seeds
    almanac.pop(0)
    #Create a map for each conversion category
    #Remove map names
    almanac = [x[1:] for x in almanac]
    #For each seed, go through the maps to convert the source per almanac.
    return findLowestLocation(almanac, seeds)

def getSolutionPart1(input_file):
    almanac = pathlib.Path(input_file).read_text().split('\n\n')
    almanac = [x.split("\n") for x in almanac]
    lowestLocation = process_almanac(almanac)
    return lowestLocation

def getSolutionPart2(input_file):
    almanac = pathlib.Path(input_file).read_text().split('\n\n')
    almanac = [x.split("\n") for x in almanac]
    lowestLocation = find_lowest_location_within_seeds(almanac)
    return lowestLocation


#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))
    

    
if __name__ == '__main__':
    main('input.txt')