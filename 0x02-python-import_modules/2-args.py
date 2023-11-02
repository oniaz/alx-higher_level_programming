#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    s = "s"
    end = ":"
    length = len(argv) - 1
    if not length:
        end = "."
    elif length == 1:
        s = ""
    print("{} argument{}{}".format(length, s, end))

    for i in range(1, length + 1):
        print("{}: {}".format(i, argv[i]))
