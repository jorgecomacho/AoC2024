filename = 'day02.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def listify(data):
    res = []
    for line in data:
        res.append(list(map(int, line.split())))
    return res

def safe(row):
    if row != sorted(row) and row[::-1] != sorted(row):
        return False
    print(row)
    for i in range(1, len(row)):
        if not 0 < abs(row[i] - row[i-1]) < 4:
            return False
    return True
    
if __name__ == "__main__":
    lines = read_file(filename)
    res = listify(lines)
    part1 = 0
    part2 = 0
    for line in res:
        if safe(line):
            part1 += 1
            continue
        for i in range(len(line)):
            if safe(line[:i] + line[i+1:]):
                part2 += 1
                break
    print(part1, part1 + part2)