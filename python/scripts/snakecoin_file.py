import hashlib
import os
import datetime as date

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
    # Manually construct a block with
    # index zero and arbitrary previous hash
    return Block(file_name, date.datetime.now(), "GenesisFile")



def next_block(file_name, last_block):
    this_name = file_name
    this_timestamp = date.datetime.now()
    this_hash = last_block.hash
    return Block(this_name, this_timestamp, this_hash)



# Create the blockchain and add the genesis block
blockchain = [create_genesis_block('snakecoin_file.py')]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for f in os.listdir('.'):
    if os.path.isfile(f):
        block_to_add = next_block(f, previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        # Tell everyone about it!
        print "Block {} has been added to the blockchain!".format(block_to_add.name)
        print "Hash: {}".format(block_to_add.hash)
        print "Previous Hash: {}\n".format(block_to_add.previous_hash)
