import os

from module.submod.submod1 import asd

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)


def add(a, b):
    return a+b

def main():
    print(add(3, 7))
    print(os.getcwd())
    asd()

main()