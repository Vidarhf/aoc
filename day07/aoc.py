
from os import environ
import pathlib
from functools import reduce

HandStrength = {
    'five of a kind': 6,
    'four of a kind': 5,
    'full house': 4,
    'three of a kind': 3,
    'two pair': 2,
    'one pair': 1,
    'highest card': 0
}

def getHandStrength(hand):
    for char in set(hand):
        if hand.count(char) == 5:
            return HandStrength['five of a kind']
        elif hand.count(char) == 4:
            return HandStrength['four of a kind']
        elif hand.count(char) == 3:
            #Check for full house
            for char2 in set(hand):
                if hand.count(char2) == 2 and char != char2:
                    return HandStrength['full house']
            return HandStrength['three of a kind']
        elif hand.count(char) == 2:
            #Check for full house
            for char2 in set(hand):
                if hand.count(char2) == 3 and char != char2:
                    return HandStrength['full house']
            #Check for two pair
            for char2 in set(hand):
                if hand.count(char2) == 2 and char != char2:
                    return HandStrength['two pair']
            return HandStrength['one pair']
    return HandStrength['highest card']

def getOnlyJokerStrength(hand):
    jokers = hand.count("J")
    if jokers == 0:
        return 0
    if jokers == 1:
        return HandStrength['one pair']
    elif jokers == 2:
        return HandStrength['three of a kind']
    elif jokers == 3:
        return HandStrength['four of a kind']
    elif jokers == 4 or jokers == 5:
        return HandStrength['five of a kind']

def getJokerHandStrength(hand):
    #Check for joker(s)
    jokers = hand.count("J")
    bestHand = HandStrength['highest card']
    for i in range(0, len(hand)):
        char = hand[i]
        if char == "J":
            continue
        if hand.count(char) == 5-jokers:
            bestHand = max(HandStrength['five of a kind'], bestHand)
        elif hand.count(char) == 4-jokers:
            bestHand = max(HandStrength['four of a kind'], bestHand)
        elif hand.count(char) == 3-jokers:
            #Check for full house
            for char2 in set(hand):
                if hand.count(char2) == 2 and char != char2 and char2 != "J":
                    bestHand = max(HandStrength['full house'], bestHand)
            bestHand = max(HandStrength['three of a kind'], bestHand)
        elif hand.count(char) == 2:
            #Check for four of a kind
            if(jokers == 2):
                bestHand = max(HandStrength['four of a kind'], bestHand)
            #Check for full house
            if(jokers == 3):
                bestHand = max(HandStrength['full house'], bestHand)
            for char2 in set(hand):
                if hand.count(char2) == 3 and char != char2:
                    bestHand = max(HandStrength['full house'], bestHand)
            #Check for two pair
            for char2 in set(hand):
                if hand.count(char2) == 2-jokers and char != char2:
                    bestHand = max(HandStrength['two pair'], bestHand)
            bestHand = max(HandStrength['one pair'], bestHand)
    return bestHand

def sortHandsByHighestCard(handBids, cardValues):
    newArr = handBids
    swapped = False
    for n in range(len(handBids)-1, 0, -1):
        for i in range(n):
            # Compare and only sort if the hands have the same strength
            if newArr[i][1] == newArr[i + 1][1]:
                # Compare the highest card left to right
                for(char1, char2) in zip(newArr[i][0], newArr[i+1][0]):
                    if cardValues[char1] < cardValues[char2]:
                        newArr[i], newArr[i + 1] = newArr[i + 1], newArr[i]
                        swapped = True
                        break
                    elif cardValues[char1] > cardValues[char2]:
                        break 
        if not swapped:
            # exiting the function if we didn't make a single swap
            # meaning that the array is already sorted.
            break
    return newArr

def calculateTotalWinnings(handBids):
    totalWinnings = 0
    numberOfHands = len(handBids)
    #Iterate over all hands, multiplting bid amount with the number of hands - the hand index
    for i in range(0, numberOfHands):
        totalWinnings += (handBids[i][2] * (numberOfHands - i))
    return totalWinnings

def process_input(input_file):
    input = pathlib.Path(input_file).read_text().split('\n')
    handBids = [[line.split()[0], getHandStrength(line.split()[0]), int(line.split()[1])] for line in input]
    #Sort by winning hands
    handBids.sort(key=lambda x: x[1], reverse=True)
    #Sort identical hands by highest card
    winners = sortHandsByHighestCard(handBids, {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"T":10, "J":11, "Q":12, "K":13, "A":14})
    totalWinning = calculateTotalWinnings(winners)
    
    return totalWinning

def process_input2(input_file):
    input = pathlib.Path(input_file).read_text().split('\n')
    handBids = [[line.split()[0], max(getJokerHandStrength(line.split()[0]), getOnlyJokerStrength(line.split()[0])), int(line.split()[1])] for line in input]
    #Sort by winning hands
    handBids.sort(key=lambda x: x[1], reverse=True)
    #Sort identical hands by highest card
    winners = sortHandsByHighestCard(handBids, {"2": 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9,"T":10, "J":1, "Q":12, "K":13, "A":14})
    totalWinning = calculateTotalWinnings(winners)
    
    return totalWinning

def getSolutionPart1(input_file):
    totalWinnings = process_input(input_file)
    return totalWinnings

def getSolutionPart2(input_file):
    totalWinnings = process_input2(input_file)
    return totalWinnings


#Main from Cygni python template
def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))

if __name__ == '__main__':
    main('input.txt')