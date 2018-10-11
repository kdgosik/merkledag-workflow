#!/usr/bin/env python

import merkledag
import sys
import argparse

# initiate the parser
parser = argparse.ArgumentParser(description='Hash link two or more files together')

# add long and short argument (args.width)
parser.add_argument("--input", "-i", help="Input file to hash")

# add long and short argument (args.width)
parser.add_argument("--link", "-l", nargs = '*', help="List of files to hash link to input file.", default = [])#, action = 'append')

# read arguments from the command line
args = parser.parse_args()

def main():
    data_file = args.input
    print(data_file)
    previous_list = args.link
    print(previous_list)
    print(merkledag.add_block(data_file, previous_list))


if __name__ == '__main__':
    main()
