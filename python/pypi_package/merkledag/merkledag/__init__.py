"""Creating merkle dag helper functions
The purpose of this is to create helper functions that will run hashing functions to create a merkle dag of while working.
It is meant to ease in documenting and tracking of creation of files and how they fit together in a network.

"""
from .merkledag import *


import hashlib
import os
import datetime as date


def hash_file(file_to_hash, BLOCKSIZE=65536, hasher=hashlib.sha256()):

    with open(file_to_hash, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return(hasher.hexdigest())



if __name__ == "__main__":
    import sys

    ## mock example
    new_block_list = []
    for a in sys.argv:
        new_block_list.append(create_genesis_block(a))

    ## hashes output file and connects it to all input files
    output_block = next_block('output_name.txt', new_block_list)
