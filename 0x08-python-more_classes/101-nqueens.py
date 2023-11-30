#!/usr/bin/python3
import sys
"""A module that solves the N queens problem"""

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

n = sys.argv[1]

if not n.isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(n)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)
