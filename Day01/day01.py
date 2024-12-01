filename = 'day01.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def one(data):
    total = 0
    left = []
    right = []
    for line in data:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    for a, b in zip(sorted(left), sorted(right)):
        total += abs(a-b)
    return total

def two(data):
    total = 0
    left = []
    right = []
    for line in data:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    for a in left:
        total += a * right.count(a)
    return total

if __name__ == "__main__":
    lines = read_file(filename)
    print(one(lines))
    print(two(lines))