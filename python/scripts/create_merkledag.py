import pandas as pd
import os
import time
import hash_file

# type Block struct {
#   Name string
#   Timestamp string
#   Hash string
#   PrevHash string
# }

# Initalising the dictionary
merkledag = []

# Filling the dictionary
for f in os.listdir('.'):
    if os.path.isfile(f):
        name = f
        timestamp = time.time()
        hash = hash_file.hash_file(f)
        prevhash = ''

        merkledag.append({"Name" : name, "Timestamp" : timestamp, "Hash" : hash, "PrevHash": prevhash})


# creating a dataframe of the merkledag
df = pd.DataFrame(merkledag)
df.to_csv("PracticeDAG.csv", index = False)
