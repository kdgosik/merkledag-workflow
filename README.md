# Merkle DAG Workflow
[Reference](https://blockchaindemo.io/)

## Concept

Create an (decentralized?) application to create a connected workflow as it is developed, instead of retrospectively.


## Steps


### Adapt Demo

Adapt the blockchaindemo.io app to be able to have a broader input space to being more than data


### Allow Forking

Allow the blockchain app to fork turning it into a merkle dag.  Having branches are necessary


### Create Mine Button

Create a mine button capability that connects to or links with Jupyter notebooks to execute the command portions.  This will allow for commands to be run in common jupyter kernels like R, python and bash.


### Save Blocks


#### JSON

Save each block into a json object list.  This will allow for easier searching in the future


#### IPFS

Save blocks into IPFS to create an automatic hash and storage of each of the blocks.


### Mine to WDL

Create a mining capability to connect to WDL.  Each block will be a task in WDL.  Runtime for dockers may be necessary.


### Function to Workflow

Create a function to take a blockchain path and create a WDL workflow from the path.  It can be fed the last hash in the path and be able to traverse the blockchain to run the tasks to stitch together into a workflow.


### Search Functions


#### Dependencies

Have a search function to traverse the blockchain to find dependencies to run before being able to run a current task


#### Recommendation

Have a function for search to find Next Steps for analysis.  This can be used as a recommendation engine for next steps to take in an analysis.
