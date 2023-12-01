
from os import environ
import re


def process_line1(line):
    #Extract the first occuring and last occuring digits from the line
    first = next(int(digit) for digit in line if digit.isdigit())
    last = next(int(digit) for digit in reversed(line) if digit.isdigit())

    #Combine the digits into a number, for examnple 1 and 2 would be 12
    number = str(first) + str(last)
    return int(number)

def process_line2(line):
    #Extract the first occuring and last occuring digits from the line
    #The numbers can also be spelled out
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
        'eno': '1',
        'owt': '2',
        'eerht': '3',
        'ruof': '4',
        'evif': '5',
        'xis': '6',
        'neves': '7',
        'thgie': '8',
        'enin': '9',
        '1': '1',
        '2': '2',
        '3': '3',
        '4': '4',
        '5': '5',
        '6': '6',
        '7': '7',
        '8': '8',
        '9': '9'
    }
    #All the digits spelled out and in digit strings
    pattern = r'(one|two|three|four|five|six|seven|eight|nine|[1-9])'
    revpattern = r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[1-9])'
    #reverse patters is used to find the last occuring digit

    
    matches = re.findall(pattern, str(line).lower())
    revmatches = re.findall(revpattern, str(line[::-1]).lower())
    first_item = digit_mapping[matches[0]]
    last_item = digit_mapping[revmatches[0]]
    #Combine the digits into one number, for examnple 1 and 2 would be 12
    number = first_item + last_item
    return int(number)

def getSolutionPart1(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            total += process_line1(line)
    return total

def getSolutionPart2(input_file):
    total = 0
    with open(input_file, "r") as f:
        for line in f:
            total += process_line2(line)
    return total


def main(input_file):
    part = environ.get('part')
    if part == 'part1':
        print(getSolutionPart1(input_file))
    else:
        print(getSolutionPart2(input_file))

main('input.txt')
    