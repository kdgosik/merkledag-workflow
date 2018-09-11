import hashlib
import sys

BLOCKSIZE = 65536
hasher = hashlib.sha256()
# file_to_hash = sys.argv[1]


def hash_file(file_to_hash):
    with open(file_to_hash, 'rb') as afile:
        buf = afile.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = afile.read(BLOCKSIZE)
    return(hasher.hexdigest())

# print(hash_file(file_to_hash))
