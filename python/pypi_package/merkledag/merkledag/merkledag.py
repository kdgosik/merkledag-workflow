import hashlib
import os
import datetime as date



## TODO this may be absorbed by the class Block below.  Might need removing
def hash_file(file_to_hash, BLOCKSIZE=65536, hasher=hashlib.sha256()):

    with open(file_to_hash, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return(hasher.hexdigest())





class Block:
    def __init__(self, name, timestamp, previous_hash):
        self.name = name
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = self.hash_file()

    def hash_file(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha256()

        with open(self.name, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return(hasher.hexdigest())




def create_genesis_block(file_name):
    # Manually construct a block by giving a file name
    # TODO add to the merkle dag file from init() function below
    return Block(file_name, date.datetime.now(), "GenesisFile")



def next_block(file_name, last_block):
    # TODO add to the merkle dag file from init() function below
    # TODO extend to include multiple hashes for each file it depends on
    this_name = file_name
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    return Block(this_name, this_timestamp, this_hash)




## TODO other possible functions needed

def init():
    """
    initialize the repository to create csv and/or json file to hold the dag file of blocks.
    """



def lookup():
    """
    Look up function to see if hash and/or file already exists in merkle dag
    """



def visualizer():
    """
    create a visualizer of the merkle dag
    """


def other_cool_functions():
    """
    any other cool functions needed to make this function better?
    """
