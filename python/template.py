#!/usr/bin/env python
"""
Template script to use when running analysis to capture in a merkledag
"""
import os
import datetime as date


def function_to_run_script():
    """
    Place analysis script here
    """



if __name__ == "__main__":
    import sys
    import merkledag
    merkledag.create_genesis_block(sys.argv[0])
    merkledag.create_genesis_block(sys.argv[1])
    merkledag.next_block(sys.argv[2])
