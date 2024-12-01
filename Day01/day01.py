filename = 'day01.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def listify(data):
    left = []
    right = []
    for line in data:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    return left, right

def one(left, right):
    total = 0
    for a, b in zip(sorted(left), sorted(right)):
        total += abs(a-b)
    return total

def two(left, right):
    total = 0
    for a in left:
        total += a * right.count(a)
    return total

if __name__ == "__main__":
    lines = read_file(filename)
    left, right = listify(lines)
    print(one(left, right))
    print(two(left, right))