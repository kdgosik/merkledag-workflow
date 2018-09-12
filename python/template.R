#!/usr/bin/env Rscript
"""
Template script to use when running analysis to capture in a merkledag
"""
library(reticulate)
# os <- import("os")
# os$listdir(".")

args <- commandArgs()


function_to_run_script <- function(args) {
    """
    Place analysis script here
    """
}


function_to_run_script(args)

if __name__ == "__main__":
    import("merkledag")
    merkledag$create_genesis_block(args[0])
    merkledag$create_genesis_block(args[1])
    merkledag$next_block(args[2])
