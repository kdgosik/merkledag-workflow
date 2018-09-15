Merkle Dag
----------

Work in Progress!!



**parallels to IPFS**

create_genesis_block would be like ipfs add file

next_block would be link ipfs object add-link file

simple example script to run and ipfs procedure to follow
```
python run_script.py input.txt params.json output_file.txt
```

ipfs add run_script.py
ipfs add input.txt
ipfs add params.json
ipfs add output_file.txt

ipfs object output_file.txt add-link run_script.py
ipfs object output_file.txt add-link input.txt
ipfs object output_file.txt add-link params.json
