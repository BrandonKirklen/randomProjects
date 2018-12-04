#!/usr/bin/python
import unittest


def freqCalc(input):
    return sum(input)

def freqDouble(input):
    seenFreqs = {0}
    currentSum = 0
    found = False
    while not found:
        for x in input:
            currentSum += x
            if currentSum in seenFreqs:
                found = True
                break
            else:
                seenFreqs.add(currentSum)
    # print("Seen Freqs:" + str(seenFreqs))
    # print("currentSum:" + str(currentSum))
    return currentSum


class MyTest(unittest.TestCase):
    def test_calcs(self):
        self.assertEqual(freqCalc([1,1,1]), 3)
        self.assertEqual(freqCalc([1,1,-2]), 0)
        self.assertEqual(freqCalc([-1,-2,-3]), -6)

    def test_doubles(self):
        self.assertEqual(freqDouble([1, -1]), 0)
        self.assertEqual(freqDouble([3,3,4,-2,-4]), 10)
        self.assertEqual(freqDouble([-6,3,8,5,-6]), 5)
        self.assertEqual(freqDouble([7,7,-2,-7,-4]), 14)

def main():
    with open("/Users/brandonkirklen/Code/Personal/randomProjects/AdventOfCode2018/day1/input.txt") as f:
        content = []
        for line in f:
            if line.strip():
                content.append(int(line))
    print("Freq:                  " + str(freqCalc(content)))
    print("Freq at First Double:  " + str(freqDouble(content)))


if __name__ == '__main__':
    # unittest.main()
    main()
