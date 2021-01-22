import sys
from daily.controller import Controller


def run():
    Controller().main(sys.argv[1:])


if __name__ == '__main__':
    run()
