package main

import (
	"fmt"
  "encoding/json"
  "time"
  "strings"
  "os"

  "github.com/ipfs/go-ipfs/core"
  "github.com/ipfs/go-ipfs/core/coreunix"
	cid "github.com/ipfs/go-cid"
	mh "github.com/multiformats/go-multihash"
)

func AddFile(ipfs *core.IpfsNode, file string) (string, error) {
    fi, err := os.Open(file)
    if err != nil {
        return "", err
    }

    return coreunix.Add(ipfs, fi)
}

//TODO more complicated data structure?
//
type Block struct {
  Name string
  Timestamp string
  Hash string
  PrevHash string
}

// func calculateHash(block Block) string {
// 	record := string(block.Index) + block.Timestamp + string(block.BPM) + block.PrevHash
// 	h := sha256.New()
// 	h.Write([]byte(record))
// 	hashed := h.Sum(nil)
// 	return hex.EncodeToString(hashed)
// }


func calculateHash(block Block) string {
	record := string(block.Name) + block.Timestamp + string(block.Hash) + block.PrevHash
  c1, err := pref.Sum([]byte(record))

}

func main() {

  // TODO update for my purposes
  t := time.Now()
  genesisBlock := Block{}
  genesisBlock = Block{0, t.String(), 0, calculateHash(genesisBlock), ""}

	// Create a cid manually by specifying the 'prefix' parameters
	pref := cid.Prefix{
		Version:  1,
		Codec:    cid.Raw,
		MhType:   mh.SHA2_256,
		MhLength: -1, // default length
	}

	// And then feed it some data
	c1, err := pref.Sum([]byte("Hello World!"))
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("Created CID: ", c1)
	// Created CID:  zb2rhfE3SX3q7Ha6UErfMqQReKsmLn73BvdDRagHDM6X1eRFN

	// Create a cid from a marshaled string
	c2, err := cid.Decode("zb2rhfE3SX3q7Ha6UErfMqQReKsmLn73BvdDRagHDM6X1eRFN")
	if err != nil {
		fmt.Println(err)
	}

	fmt.Println("Got CID: ", c2)

	// To check if some data matches a given cid,
	// Get your CIDs prefix, and use that to sum the data in question:
	mydata := []byte("Hello World!!")
	other, err := c1.Prefix().Sum(mydata)
	if err != nil {
		fmt.Println(err)
	}

	if !c1.Equals(other) {
		fmt.Println("This data is different.")
	} else {
		fmt.Println("They are the same!")
	}

}
