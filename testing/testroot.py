import os
import pytest
import filecmp

def test_one():
    os.system('python3 ../root.py input/input1.txt')
    simTest("output/output1.txt")

def test_two():
    os.system('python3 ../root.py input/input2.txt')
    simTest("output/output2.txt")

def test_three():
    os.system('python3 ../root.py input/input3.txt')
    simTest("output/output3.txt")

def simTest(outFile):
    expected = open(outFile, "r")
    actual = open("output.txt", "r")
    assert expected.read() == actual.read()
    expected.close()
    actual.close()

def main():
    test_one()
    test_two()
    test_three()

if __name__== "__main__":
    main()
