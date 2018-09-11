# Merkle DAG Workflow
[Reference](https://blockchaindemo.io/)

## Concept

Create an (decentralized?) application to create a connected workflow as it is developed, instead of retrospectively.  This can be tied to something like a jupyter notebook or be its own application.  A merkle dag structure will be used the underlying storage mechanism (via (ipfs)[ipfs.io]/(ipld)[ipld.io]).  There are a few parts that need to be considered to make sure the underlying data structure is flexible but also tracks the relevant information.  As of right now the object being hashed need to contain 3 major portions.  Each major portion will be itselfed hashed and then concatenated together for the final object hash.  An analog to bitcoin would be the portions would be like transactions and objects would be the blocks.  The 3 portions to the workflow would be
  1. The input parameters
  2. The input files
  3. The software/script

Having these 3 things separated out into there own "transactions" will give greater flexibility in the search and reconstruction capability of workflows.  The interchanging of these parts is an important feature and thus important to keep them as separate hashes that are later put together.  I plan to bring together several tools in order to accomplish this.  The actual use of a blockchain may not actually be necessary but I am also not completely ruling it out.  One advantage to using a blockchain or a smart contract system would be having a mining capability.  In order to add something to the network you would have prove it ran without error with current environment(docker container), software/script, parameters, and input files necessary.  Where this may fall short is if a token would be necessary for this process to incentivize the use of the mining tool.  A distributed hash table may be enough to track this but there would be no verification done (which i think would be important).


Some of the tools I am considering using are
  - [IPFS](ipfs.io)
  - [Jupyter](http://jupyter.org/)
  - [Snakemake](https://snakemake.readthedocs.io/en/stable/)
  - [WDL](https://software.broadinstitute.org/wdl/)
  - [Docker](https://www.docker.com/)
  - [Repo2Docker](http://repo2docker.readthedocs.io/en/latest/)
    - This could be easily used to migrate any git/github software to be incorporated into a cohesive network that everyone can build together


This is a huge work in progress.  The idea is somewhat formulated but definitely open to suggestions and improvements to it. Hopefully I will be able to make progress on this.  Any help would be greatly appreciated.  Please feel free to reach out to me.  

## Steps

 Some tutorials and inspirations
   - [IPFS and Ethereum](https://www.youtube.com/watch?v=ADoRVVOSpI8&list=PLS5SEs8ZftgWggD3tKfgwsIPXuIhorXZk)
   - [Ethereum File Upload](https://snipbin.now.sh/)
   - [Python Blockchain App](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)


### Adapt Demo

Adapt something like this [demo](blockchaindemo.io) or this [one](https://gist.github.com/aunyks/47d157f8bc7d1829a729c2a6a919c173) app to be able to have a broader input space to being more than data.  Would need to accept input parameters, files, and software.


### Allow Forking

Allow the blockchain app to fork turning it into a merkle dag.  Having branches are necessary and important for people to build and grow analysis in the directions they see fit.


### Create Mine Button

Create a mine button capability that connects to or links with Jupyter notebooks to execute the command portions.  This will allow for commands to be run in common jupyter kernels like R, python and bash (others?).


### Save Blocks


#### JSON

Save each block into a json object list.  This will allow for easier searching in the future


#### IPFS

Save blocks into IPFS to create an automatic hash and storage of each of the blocks.


### Mine WDL Check

Create a mining capability to connect to [WDL](https://software.broadinstitute.org/wdl/) or snakemake.  Each block will be a task in WDL.  Runtime for dockers may be necessary.  
[jupyter-repo2docker](http://repo2docker.readthedocs.io/en/latest/)


### Function to Workflow

Create a function to take a blockchain path and create a WDL workflow from the path.  It can be fed the last hash in the path and be able to traverse the blockchain to run the tasks to stitch together into a workflow or even a jupter notebook.


### Search Functions


#### Dependencies

Have a search function to traverse the blockchain to find dependencies to run before being able to run a current task


#### Recommendation

Have a function for search to find Next Steps for analysis.  This can be used as a recommendation engine for next steps to take in an analysis.
