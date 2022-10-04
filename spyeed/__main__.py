import argparse
import os
import sys


class Spyeed:
    def __init__(self):
        pass

    def generate(self):
        dst = os.path.join(os.getcwd(), 'templates', self.ftype)
        with open(dst, 'r') as rf:
            pass

def sypeed(argv=sys.argv[2:]):
    parser = argparse.ArgumentParser()
    parser.add("--ftype", required=True)
    args = parser.parse_args(argv)

    s = Spyeed(*args)
    s.generate()

    sys.exit(0)