package main

import (
	"crypto/sha512"
	"encoding/hex"
	"fmt"
	"io/ioutil"
	"os"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Printf("Usage: %s <filename>\n", os.Args[0])
		os.Exit(1)
	}
	filename := os.Args[1]
	buff, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		return
	}
	hasher := sha512.New()
	hasher.Write(buff)
	digest := hex.EncodeToString(hasher.Sum(nil));
	fmt.Println(digest)
}