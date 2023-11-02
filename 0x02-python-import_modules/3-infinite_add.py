#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum = 0
    length = len(argv) - 1
    if length:
        for i in range(length):
            sum += int(argv[i+1])
    print(sum)
    