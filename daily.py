#!/usr/bin/python3
import sys
from core.controller import Controller


def run():
    Controller().main(sys.argv[1:])


if __name__ == '__main__':
    run()
