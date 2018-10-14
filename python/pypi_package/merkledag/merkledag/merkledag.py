#!/usr/bin/env python

import hashlib
import os
import re
import json
import datetime as date
import time
from subprocess import PIPE, run
from sys import platform

# uses internal systems checksum sha 256 algoritm
def checksum_file(name):
    if platform == "linux" or platform == "linux2":
        # linux
        command = 'sha256sum '
    elif platform == "darwin":
        # OS X
        command = 'shasum -a 256 '
    elif platform == "win32":
        # Windows
        command = 'FCIV -sha256 '

    command = command + name
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)

    out = result.stdout.split('  ')
    hash = out[0]
    return(hash)


## Block class for creating block structure
## may need to make previous_hash a list of previous hashes
class Block:
    def __init__(self, name, previous_hashes):
        self.name = os.path.basename(name)
        self.path = name
        self.timestamp = str(time.ctime(os.path.getmtime(name)))
        self.description = ''
        self.author = ''
        self.checksum = self.checksum_file()
        self.previous_hashes = sorted(previous_hashes)
        self.hash = self.hash_block()

        ## defined above
    def checksum_file(self):
        return(checksum_file(self.path))

        ## hash the entire block for refernce in next block
    def hash_block(self):
        sha = hashlib.sha256()
        sha.update((str(self.checksum) + str(self.previous_hashes)).encode('utf-8'))
        return sha.hexdigest()


## Add Block to replace create_genesis_block and next_block
def add_block(file_name, depend_files, merkledag_file = 'merkledag_file.json'):
    # if merkledag file doesn't exist, create it
    if not os.path.isfile(merkledag_file):
        merkledag = []
        ## writing with indetation for a pretty print
        with open(merkledag_file, 'w') as out_file:
            json.dump(merkledag, out_file, indent=4)

    # checks if a genesis file (no previous file dependencies)
    if depend_files == "":

        ## creates a new block
        newBlock = Block(file_name, "")

        ## add new block to merkledag file
        with open(merkledag_file, 'r') as in_file:
            merkledag = json.load(in_file)
            merkledag.append(newBlock.__dict__)

        ## writing with indetation for a pretty print
        with open(merkledag_file, 'w') as out_file:
            json.dump(merkledag, out_file, indent=4)

    else:  ## if depend are given
        previous_hashes = []
        ## loop through each dependency
        for l in depend_files:
            if lookup_hash(l):
                previous_hashes.append(l)

            else:
                file_checksum = checksum_file(l)
                file_block = lookup_file(file_checksum)
                file_block_hash = file_block['hash']
                previous_hashes.append(file_block_hash)

        newBlock = Block(file_name, previous_hashes)

        ## add new block to merkledag file
        with open(merkledag_file, 'r') as in_file:
            merkledag = json.load(in_file)
            merkledag.append(newBlock.__dict__)

        ## writing with indetation for a pretty print
        with open(merkledag_file, 'w') as out_file:
            json.dump(merkledag, out_file, indent=4)



## searches merkledag_file.json for the content hash of the file and returns it
def lookup_file(file_checksum, merkledag_file = 'merkledag_file.json'):
    out = False
    with open(merkledag_file, 'r') as in_file:
        merkledag = json.load(in_file)
    for block in merkledag:
        if block['checksum'] in file_checksum:
            out = block ## block needed
    return(out)


## searches merkledag_file.json for the block hash and returns True if found
def lookup_hash(block_hash, merkledag_file = 'merkledag_file.json'):
    out = False
    with open(merkledag_file, 'r') as in_file:
        merkledag = json.load(in_file)
    for block in merkledag:
        if block['hash'] in block_hash:
            out = True ## block needed
    return(out)





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
