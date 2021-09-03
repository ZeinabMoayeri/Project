# - print_file.py *- coding: utf-8 -*-
""" Opens file and prints its contents line by line. """

import sys     # we need this library to deal with operating system

filename = sys.argv[1]
filename2 = sys.argv[2]

infile = open(filename)
infile2 = open (filename2)

for line in infile:
    print(line,end="") # the file has "\n" at the end of each line already
for line in infile2:
    print(line, end="")
infile.close()
infile2.close()