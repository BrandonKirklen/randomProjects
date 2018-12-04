#!/usr/bin/python
import unittest

def sumMatchingAdjacent(input):
    sum = 0
    for index in range(len(input)):
        if input[index] == input[(index + 1) % len(input)]:
            sum += int(input[index])
    return sum

def sumMatchingHalfway(input):
    sum = 0
    for index in range(len(input)):
        if input[index] == input[(index + len(input) / 2) % len(input)]:
            sum += int(input[index])
    return sum


class MyTest(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(sumMatchingAdjacent("1122"), 3)
        self.assertEqual(sumMatchingAdjacent("1111"), 4)
        self.assertEqual(sumMatchingAdjacent("1234"), 0)
    def test_loop1(self):
        self.assertEqual(sumMatchingAdjacent("91212129"), 9)
    def test_simple2(self):
        self.assertEqual(sumMatchingHalfway("1212"), 6)
        self.assertEqual(sumMatchingHalfway("1221"), 0)
        self.assertEqual(sumMatchingHalfway("123425"), 4)
        self.assertEqual(sumMatchingHalfway("123123"), 12)
        self.assertEqual(sumMatchingHalfway("12131415"), 4)

def main():
    with open("day1_in") as f:
        content = [str(x) for x in next(f).split()]
    print("Solution Adjacent: " + str(sumMatchingAdjacent(content[0])))
    print("Solution Halfway:  " + str(sumMatchingHalfway(content[0])))


if __name__ == '__main__':
    main()
    unittest.main()
