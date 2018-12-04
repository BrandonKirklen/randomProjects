#!/usr/bin/python
import unittest

testArray = [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]

def checkSum(input):
    biggest = [max(x) for x in input]
    smallest = [min(x) for x in input]
    difference = [i - j for i, j in zip(biggest, smallest)]
    return sum(difference)


def main():
    content = []
    with open("day2_in") as f:
        for row in f:
            content.append(map(int, row.strip().split()))
    print checkSum(content)



if __name__ == '__main__':
    main()
