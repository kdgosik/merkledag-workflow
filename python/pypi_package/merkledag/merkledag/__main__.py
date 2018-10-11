#!/usr/bin/env python

import merkledag
import sys
import argparse

# initiate the parser
parser = argparse.ArgumentParser(description='Hash link two or more files together')

# add file input argument (args.input)
parser.add_argument("--input", "-i", help="Input file to hash")

# add list of links argument (args.link)
parser.add_argument("--link", "-l", nargs = '*', help="List of files to hash link to input file.", default = [])#, action = 'append')

# add output file name argument (args.output)
parser.add_argument("--output", "-o", nargs = '?', help="Ouput file name (defualts to ./merkledag_file.json).", default = 'merkledag_file.json')#, action = 'append')

# read arguments from the command line
args = parser.parse_args()

def main():
    data_file = args.input
    print('Added '+ data_file + ' to the merkle dag!')
    previous_list = args.link
    print('Linked ' + data_file + ' to the file(s): ' + ', '.join(previous_list))
    output_file = args.output
    print('Placed output in ' + output_file)
    merkledag.add_block(data_file, previous_list, output_file)


if __name__ == '__main__':
    main()
