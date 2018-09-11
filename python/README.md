## Intro

Create a block object containing name, timestamp, hash and previous hash.
[Reference](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)

[Jupyter Server Extensions](https://jupyter-notebook.readthedocs.io/en/stable/extending/handlers.html#writing-a-notebook-server-extension)

[Reference](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Distributing%20Jupyter%20Extensions%20as%20Python%20Packages.html#Defining-the-server-extension-and-nbextension)


a simple structure of the merkle dag will most likely look something like

dataset -> script -> dataset -> script -> ...

## TODO

  - Create block generator
  - Link blocks together
  - How to trigger a block generation
  - Create script from each jupyter notebook cell?
  - How to update a script with input parameters and datasets
  - Look up function for scripts/datasets
    - save a script with input hashes and parameters
    - replace hashes(programmatically) with file names when running a script?
    - will need how to look up hashes and/or files when working
