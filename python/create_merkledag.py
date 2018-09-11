import pandas as pd
import os
import hash_file

# Initalising the dictionary
reviews = {}

# Filling the dictionary
for line in lines:
  l = line.strip().split("\t")

  # These are just training wheels to see more clearly what goes into the dictionary
  score = l[0]
  id = l[1]
  title = l[2]
  review = l[3]

  reviews[id] = {"score" : score, "title" : title, "review" : review}



merkledag = [{}]
df = pd.DataFrame(merkledag)
