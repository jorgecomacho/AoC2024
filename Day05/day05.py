filename = 'day05.txt'
#filename = 'test.txt'

import os
from functools import cmp_to_key

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

lines = read_file(filename)

rules= []
updates = []
for line in lines:
    if '|' in line:
        rules.append(list(map(int,line.split('|'))))
    if ',' in line:
        updates.append(list(map(int,line.split(','))))

def comp_em(first, second):
    okay = True
    for rule in rules:
        if first == rule[0] and second == rule[1]:
            continue
        if first == rule[1] and second == rule[0]:
            return 1
    return -1

def huh(lines):
    p1 = 0
    p2 = 0
    key_function = cmp_to_key(comp_em)
    for update in updates:
        if update == sorted(update, key=key_function):
            p1 += update[int(len(update)/2)]
        else:
            p2 += sorted(update, key=key_function)[int(len(update)/2)]
    print(p1, p2)

if __name__ == "__main__":
    huh(lines)