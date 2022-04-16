import sys
from solver import Solver
from parser import Parser

def main(args):
    if len(args) != 2:
        print("Wrong number of argument")
        return 1
    try:
        s = Parser(args[1])
        token = s.parse_token()
        print(token)
    except Exception as e:
        print(e)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
