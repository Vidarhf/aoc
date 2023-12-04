
from os import environ
import re

GREEN_MAX = 13
RED_MAX = 12
BLUE_MAX = 14


def process_line(line):
    # Find the game number
    gameSplit = line.split(":")
    # Split the line into winning and our numbers
    numbersSplit = gameSplit[1].split("|")
    winningNumbers = numbersSplit[0].strip().split(" ")
    ourNumbers = numbersSplit[1].strip().split(" ")

    total = 0
    for winningNumber in winningNumbers:
        for ourNumber in ourNumbers:
            if (winningNumber.isdigit() == False or ourNumber.isdigit() == False):
                continue
            if winningNumber == ourNumber:
                if(total > 0):
                    total = total * 2
                else:
                    total = 1
    return(total)

def process_line2(line):
    # Find the game number
    gameSplit = line.split(":")
    # Split the line into winning and our numbers
    numbersSplit = gameSplit[1].split("|")
    winningNumbers = numbersSplit[0].strip().split(" ")
    ourNumbers = numbersSplit[1].strip().split(" ")
    # it would then win a copy of the same cards that the original card 10 won: cards 11, 12, 13, 14, and 15. 
    # This process repeats until none of the copies cause you to win any more cards. (Cards will never make you copy a card past the end of the table.)
    total = 0
    for winningNumber in winningNumbers:
        for ourNumber in ourNumbers:
            if (winningNumber.isdigit() == False or ourNumber.isdigit() == False):
                continue
            if winningNumber == ourNumber:
                total += 1
    return(total)

def getSolutionPart1(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            total += process_line(line)
    return total

def getSolutionPart2(input_file):
    total = 0
    scratchCards = {i: 1 for i in range(1, 215)}
    cardNumber = 1
    with open(input_file, "r") as f:
        for line in f:
            cardLine = line
            if cardNumber in scratchCards:
                data = process_line2(cardLine)
                for run in range(scratchCards[cardNumber]):
                    for i in range(1, data+1):
                        if cardNumber + i in scratchCards:
                            modifiedValue = scratchCards[cardNumber + i] + 1
                            scratchCards.update({cardNumber+i : modifiedValue})
                        else:
                            scratchCards.update({cardNumber+i : 1})    
                total += scratchCards[cardNumber]
            else:
                break
            cardNumber += 1
    return total
   

#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))
    

main('input.txt')
    