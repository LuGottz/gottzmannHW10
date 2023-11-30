"""
reconstructSentence.py

Description: reads two text files and reconstructs their contents to produce the complete output.

Command Line Arguments: inputfile1 inputfile2

Example Invocation: python3 reconstructSentence.py input1.txt input2.txt

"""

import sys

with open(sys.argv[1]) as file1, open(sys.argv[2]) as file2:
    
    line1 = file1.readline()
    list1 = line1.split()
    length1 = len(list1)
    
    line2 = file2.readline()
    list2 = line2.split()
    length2 = len(list2)
    
    out = [None]*(length1 + length2)
    out[::2] = list1[::-1]
    out[1::2] = list2[::-1]
    
    print("list1 is: " + str(list1))
    print("list1 length: " + str(length1))
    print("")
    print("list2 is: " + str(list2))
    print("list2 length: " + str(length2))
    print("")
    print("the list out is: " + str(out))