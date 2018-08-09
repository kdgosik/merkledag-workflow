'use strict';
//const Block = require("./Block.js");
//const crypto = require("crypto");
//const crypto = require("https://cdnjs.cloudflare.com/ajax/libs/crypto-js/3.1.9-1/crypto-js.js")


class Block {
  constructor (index, previousHash, timestamp, data, hash, nonce) {
    this.index = index;
    this.previousHash = previousHash;
    this.timestamp = timestamp;
    this.data = data;
    this.hash = hash;
    this.nonce = nonce;
  }

  static get genesis() {
    return new Block(
      0,
      "0",
      1508270000000,
      "Welcome to Blockchain Demo 2.0!",
      "000dc75a315c77a1f9c98fb6247d03dd18ac52632d7dc6a9920261d8109b37cf",
      604
    );
  }
};

class Blockchain {
  constructor() {
    this.blockchain = [Block.genesis];
    this.difficulty = 3;
  }

  get() {
    return this.blockchain;
  }

  get latestBlock() {
    return this.blockchain[this.blockchain.length - 1];
  }

  isValidHashDifficulty(hash) {
    for (var i = 0; i < hash.length; i++) {
      if (hash[i] !== "0") {
        break;
      }
    }
    return i >= this.difficulty;
  }

  calculateHashForBlock(block) {
    const { index, previousHash, timestamp, data, nonce } = block;
    return this.calculateHash(
      index,
      previousHash,
      timestamp,
      data,
      nonce
    );
  }

  calculateHash(index, previousHash, timestamp, data, nonce) {
    return crypto
      .createHash("sha256")
      .update(index + previousHash + timestamp + data + nonce)
      .digest("hex");
  }

  mine(data) {
    const newBlock = this.generateNextBlock(data);
    try {
      this.addBlock(newBlock);
    } catch(err) {
      throw err;
    }
  }

  generateNextBlock(data) {
    const nextIndex = this.latestBlock.index + 1;
    const previousHash = this.latestBlock.hash;
    let timestamp = new Date().getTime();
    let nonce = 0;
    let nextHash = this.calculateHash(
      nextIndex,
      previousHash,
      timestamp,
      data,
      nonce
    );

    while (!this.isValidHashDifficulty(nextHash)) {
      nonce = nonce + 1;
      timestamp = new Date().getTime();
      nextHash = this.calculateHash(
        nextIndex,
        previousHash,
        timestamp,
        data,
        nonce
      );
    }

    const nextBlock = new Block(
      nextIndex,
      previousHash,
      timestamp,
      data,
      nextHash,
      nonce
    );

    return nextBlock;
  }

  addBlock(newBlock) {
    if (this.isValidNextBlock(newBlock, this.latestBlock)) {
      this.blockchain.push(newBlock);
    } else {
      throw "Error: Invalid block";
    }
  }

  isValidNextBlock(nextBlock, previousBlock) {
    const nextBlockHash = this.calculateHashForBlock(nextBlock);

    if (previousBlock.index + 1 !== nextBlock.index) {
      return false;
    } else if (previousBlock.hash !== nextBlock.previousHash) {
      return false;
    } else if (nextBlockHash !== nextBlock.hash) {
      return false;
    } else if (!this.isValidHashDifficulty(nextBlockHash)) {
      return false;
    } else {
      return true;
    }
  }

  isValidChain(chain) {
    if (JSON.stringify(chain[0]) !== JSON.stringify(Block.genesis)) {
      return false;
    }

    const tempChain = [chain[0]];
    for (let i = 1; i < chain.length; i = i + 1) {
      if (this.isValidNextBlock(chain[i], tempChain[i - 1])) {
        tempChain.push(chain[i]);
      } else {
        return false;
      }
    }
    return true;
  }

  isChainLonger(chain) {
    return chain.length > this.blockchain.length;
  }

  replaceChain(newChain) {
    if (this.isValidChain(newChain) && this.isChainLonger(newChain)) {
      this.blockchain = JSON.parse(JSON.stringify(newChain));
    } else {
      throw "Error: invalid chain";
    }
  }

    //TODO update to match this blockchain.js style
  updateState(block, chain) {
  // set the well background red or green for this block
    if ($('#block'+block+'chain'+chain+'hash').val().substr(0, difficulty) === pattern) {
      $('#block'+block+'chain'+chain+'well').removeClass('well-error').addClass('well-success');
    }
    else {
      $('#block'+block+'chain'+chain+'well').removeClass('well-success').addClass('well-error');
    }
  }
};

// function to add a div element to display a block
function addDivBlock() {

  var data;

  data = document.getElementById("blockdata").value;

  var div = document.createElement("DIV");
  div.classList.add("block");

  // Block Index
  var block_label = document.createElement("label");
  block_label.innerHTML = "Block:";
  div.appendChild(block_label);

  var index_textarea = document.createElement("textarea");
  div.appendChild(index_textarea);

  // Data
  var data_label = document.createElement("label");
  data_label.innerHTML = "Data:";
  div.appendChild(data_label);

  var data_textarea = document.createElement("textarea");
  data_textarea.innerHTML = data;
  div.appendChild(data_textarea);

  // Hash
  var hash_label = document.createElement("label");
  hash_label.innerHTML = "Hash:";
  div.appendChild(hash_label);

  var hash_textarea = document.createElement("textarea");
  div.appendChild(hash_textarea);

  // Previous Hash
  var prevhash_label = document.createElement("label");
  prevhash_label.innerHTML = "Previous Hash:";
  div.appendChild(prevhash_label);

  var prevhash_textarea = document.createElement("textarea");
  //prevhash.innerHTML = calculateHashForBlock();
  div.appendChild(prevhash_textarea);

  // add to DOM
  document.getElementById("container").appendChild(div);

}


//module.exports = Blockchain;
