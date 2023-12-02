
from os import environ
import re

GREEN_MAX = 13
RED_MAX = 12
BLUE_MAX = 14


    #Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes.
def process_line(line):
    # Find the game number
    gameSplit = line.split(":")
    gameId = str(gameSplit[0]).split(" ")[1]
    # Split the line based on peeks
    peeks = gameSplit[1].split(";")
    for peek in peeks:
        colorSplit = peek.split(",")
        # Find and separate the number of balls on each line depending on color
        for color in colorSplit:
            numberColor = color.split(" ")
            number = numberColor[1]
            color = numberColor[2]

            color = color.strip("\n")
            color = color.strip(",")

            if(color == "red"):
                if(int(number) > RED_MAX):
                    return 0
            if(color == "green"):
                if(int(number) > GREEN_MAX):
                    return 0
            if(color == "blue"):
                if(int(number) > BLUE_MAX):
                    return 0
    return(int(gameId))

def process_line2(line):
    gameSplit = line.split(":")
    # Split the line based on peeks
    peeks = gameSplit[1].split(";")
    #fewest number of cubes of each color that could have been in the bag to make the game possible?
    red = 0
    green = 0
    blue = 0
    for peek in peeks:
        colorSplit = peek.split(",")
        for color in colorSplit:
            numberColor = color.split(" ")
            number = numberColor[1]
            color = numberColor[2]

            color = color.strip("\n")
            color = color.strip(",")
            if(color == "red" and int(number) > red):
                red = int(number)
            if(color == "green" and int(number) > green):
                green = int(number)
            if(color == "blue" and int(number) > blue):
                blue = int(number)

    totalPower = red * green * blue
    return(totalPower)

def getSolutionPart1(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            total += process_line(line)
    return total

def getSolutionPart2(input_file):
    #what is the fewest number of cubes of each color that could have been in the bag to make the game possible?
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            total += process_line2(line)
    return total
   

#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))
    

main('input.txt')
    