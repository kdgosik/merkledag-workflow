#!/usr/bin/env python

import hashlib
import os
import json
import datetime as date
import time

## chunks a file and hashes the content
def hash_file(name):
    BLOCKSIZE = 65536
    sha = hashlib.sha256()
    with open(name, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            sha.update(buf)
            buf = afile.read(BLOCKSIZE)
    return(sha.hexdigest())



## Block class for creating block structure
## may need to make previous_hash a list of previous hashes
class Block:
    def __init__(self, name, previous_hashes):
        self.name = name
        self.timestamp = str(time.ctime(os.path.getmtime(name)))
        self.data = self.hash_file()
        self.previous_hashes = sorted(previous_hashes)
        self.hash = self.hash_block()

        ## defined above
    def hash_file(self):
        return(hash_file(self.name))

        ## hash the entire block for refernce in next block
    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.data) + str(self.previous_hashes)).encode('utf-8'))
        return sha.hexdigest()


## Add Block to replace create_genesis_block and next_block
def add_block(file_name, depend_files, output_file = 'merkledag_file.json'):
    # if merkledag file doesn't exist, create it
    if not os.path.isfile(output_file):
        d = []
        ## writing with indetation for a pretty print
        with open('merkledag_file.json', 'w') as out_file:
            json.dump(d, out_file, indent=4)

    # checks if a genesis file (no previous file dependencies)
    if depend_files == "":

        ## creates a new block
        newBlock = Block(file_name, "")

        ## add new block to merkledag file
        with open(output_file, 'r') as in_file:
            d = json.load(in_file)
            d.append(newBlock.__dict__)

        ## writing with indetation for a pretty print
        with open(output_file, 'w') as out_file:
            json.dump(d, out_file, indent=4)

    else:  ## if depend are given
        previous_hashes = []
        ## loop through each dependency
        for l in depend_files:
            file_data_hash = hash_file(l)
            file_block = lookup_file(file_data_hash)
            file_block_hash = file_block['hash']
            previous_hashes.append(file_block_hash)

        newBlock = Block(file_name, previous_hashes)

        ## add new block to merkledag file
        with open(output_file, 'r') as in_file:
            d = json.load(in_file)
            d.append(newBlock.__dict__)

        ## writing with indetation for a pretty print
        with open(output_file, 'w') as out_file:
            json.dump(d, out_file, indent=4)



## searches merkledag_file.json for the content hash of the file and returns it
def lookup_file(file_data_hash):
    with open('merkledag_file.json', 'r') as in_file:
        d = json.load(in_file)
    for i in d:
        if i['data'] in file_data_hash:
            return(i) ## file content hash








## TODO other possible functions needed



## possible function create a python script from a template and jupyter cell that incorporates the merkledag
def jupyter_cell_to_script():
    """
    script to make a jupyter notebook cell into an independent python script using template.py
    """




def visualizer():
    """
    create a visualizer of the merkle dag
    """


def other_cool_functions():
    """
    any other cool functions needed to make this function better?
    """
