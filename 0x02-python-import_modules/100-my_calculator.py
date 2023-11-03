#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = argv[2]
    if op not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    from calculator_1 import add, sub, mul, div
    a = int(argv[1])
    b = int(argv[3])

    if op == '+':
        result = add(a, b)
    if op == '-':
        result = sub(a, b)
    if op == '*':
        result = mul(a, b)
    if op == '/':
        result = div(a, b)
    print(f"{a} {op} {b} = {result}")
