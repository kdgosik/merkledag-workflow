package main

import (
    "os"

    "github.com/ipfs/go-ipfs/core"
    "github.com/ipfs/go-ipfs/core/coreunix"
)

func AddFile(ipfs *core.IpfsNode, file string) (string, error) {
    fi, err := os.Open(file)
    if err != nil {
        return "", err
    }

    return coreunix.Add(ipfs, fi)
}

func main() {



}
