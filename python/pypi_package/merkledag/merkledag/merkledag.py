import hashlib
import os
import json
import datetime as date


## Block class for creating block structure
## TODO include previous_hash when hashing the file?
## may need to make previous_hash a list of previous hashes
class Block:
    def __init__(self, name, timestamp, previous_hashes):
        self.name = name
        self.timestamp = str(timestamp)
        self.data = self.hash_file()
        self.previous_hashes = sorted(previous_hashes)
        self.hash = self.hash_block()

    def hash_file(self):
        BLOCKSIZE = 65536
        hasher = hashlib.sha256()
        with open(self.name, 'rb') as afile:
            buf = afile.read(BLOCKSIZE)
            while len(buf) > 0:
                hasher.update(buf)
                buf = afile.read(BLOCKSIZE)
        return(hasher.hexdigest())

        ## TODO not sure if I need to include the timestamp
    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.name) +
                   # str(self.timestamp) +
                   str(self.data) +
                   str(self.previous_hashes))
        return sha.hexdigest()





## genesis block creation function
## TODO how to create genesis block for each script and raw data file
## TODO differentiate between script and datasets at the hash level?
def create_genesis_block(file_name):
    # Manually construct a block by giving a file name
    # TODO add error checking
    newBlock = Block(file_name, date.datetime.now(), ['GenesisFile'])

    ## add new block to merkledag file
    with open('merkledag_file.json', 'r') as in_file:
        d = json.load(in_file)
        d.append(newBlock.__dict__)

    ## writing with indetation for a pretty print
    with open("merkledag_file.json", "w") as out_file:
        json.dump(d, out_file, indent=4, sort_keys=True)

    return newBlock



## link a new file to an existing block
## TODO input a list of last_blocks to link together?
## Would the file name in this case be the output of running the script?
def next_block(file_name, last_block):
    # TODO extend to include multiple hashes for each file it depends on
    this_name = file_name
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    newBlock = Block(this_name, this_timestamp, this_hash)

    ## add new block to merkledag file
    with open('merkledag_file.json', 'r') as in_file:
        d = json.load(in_file)
        d.append(newBlock.__dict__)

    ## writing with indetation for a pretty print
    with open("merkledag_file.json", "w") as out_file:
        json.dump(d, out_file, indent=4, sort_keys=True)

    return newBlock




## TODO other possible functions needed

## initialization function to create merkledag file
def init():
    """
    initialize the repository to create csv and/or json file to hold the dag file of blocks.
    """
    out = [{'name': 'root', 'timestamp': str(date.datetime.now()), 'hash': 'GenesisFile', 'previous_hash': ''}]
    outjson = json.dumps(out)
    with open("merkledag_file.json", "w") as f:
        f.write(outjson)



## possible function create a python script from a template and jupyter cell that incorporates the merkledag
def jupyter_cell_to_script():
    """
    script to make a jupyter notebook cell into an independent python script using template.py
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
