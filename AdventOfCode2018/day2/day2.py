#!/usr/bin/python
import unittest

def checksum(arrayOfBoxes):
    twoLetterBoxes = 0
    threeLetterBoxes = 0
    for box in arrayOfBoxes:
        counterResult = stringCounter(box)
        if counterResult["twoLetters"]:
            twoLetterBoxes += 1
        if counterResult["threeLetters"]:
            threeLetterBoxes += 1
    return twoLetterBoxes * threeLetterBoxes

def stringCounter(string):
    resultTuple = {"twoLetters": False, "threeLetters": False}
    for letter in string:
        if string.count(letter) == 2:
            resultTuple["twoLetters"] = True
        if string.count(letter) == 3:
            resultTuple["threeLetters"] = True
    return resultTuple

def commonLetters(arrayOfBoxes):
    closeWords = set()
    for box in arrayOfBoxes:
        isMatch = almostEqual(arrayOfBoxes, box)
        if isMatch:
            closeWords.add(isMatch)
            closeWords.add(box)
    return closeWords



def almostEqual(testSet, testWord):
    for word in testSet:
        count = 0
        for a, b in zip(word, testWord):
            count += a != b
            if count == 2:
                break
        if count == 1:
            return word
    else:
        return 

class MyTest(unittest.TestCase):
    def test_checksum(self):
        self.assertEqual(checksum(["abcdef","bababc","aabbcde","abcccd","aabcdd","abcdee","ababab"]), 12)


    def test_stringCounter(self):
        self.assertEqual(stringCounter("abcdef"), {"twoLetters": False, "threeLetters": False})
        self.assertEqual(stringCounter("bababc"), {"twoLetters": True, "threeLetters": True})
        self.assertEqual(stringCounter("abbcde"), {"twoLetters": True, "threeLetters": False})
        self.assertEqual(stringCounter("abcccd"), {"twoLetters": False, "threeLetters": True})
        self.assertEqual(stringCounter("aabcdd"), {"twoLetters": True, "threeLetters": False})
        self.assertEqual(stringCounter("abcdee"), {"twoLetters": True, "threeLetters": False})
        self.assertEqual(stringCounter("ababab"), {"twoLetters": False, "threeLetters": True})

    def test_commonLetters(self):
        self.assertEqual(commonLetters(["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]), "fgij")

def main():
    with open("/Users/brandonkirklen/Code/Personal/randomProjects/AdventOfCode2018/day2/input.txt") as f:
        content = []
        for line in f:
            if line.strip():
                content.append(str(line).rstrip())
    print("Checksum:                       " + str(checksum(content)))
    print("Common Letters of Correct Box:  " + str(commonLetters(content)))


if __name__ == '__main__':
    # unittest.main()
    main()
