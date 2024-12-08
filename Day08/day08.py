filename = 'day08.txt'
#filename = 'test.txt'

import os
from itertools import combinations

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def make_grid(lines):
    new_grid = {}
    for i, line in enumerate(lines):
        for j, value in enumerate(line):
            new_grid[(i,j)] = value
    return new_grid

def find_res(first, second):
    x_offset = first[0] - second[0]
    y_offset = first[1] - second[1]
    new_1 = (first[0] + x_offset, first[1] + y_offset)
    new_2 = (second[0] - x_offset, second[1] - y_offset)
    return [new_1, new_2]

def p2(first, second, grid):
    new_list = [first, second]
    x_offset = first[0] - second[0]
    y_offset = first[1] - second[1]
    tmp = first
    while True:
        tmp = (tmp[0] + x_offset, tmp[1] + y_offset)
        if tmp in grid.keys():
            new_list.append(tmp)
        else:
            break
    tmp = second
    while True:
        tmp = (tmp[0] - x_offset, tmp[1] - y_offset)
        if tmp in grid.keys():
            new_list.append(tmp)
        else:
            break
    return new_list


def build_it(grid):
    values = {'#':[]}
    for k in grid.keys():
        if grid[k] in values:
            values[grid[k]].append(k)
        else:
            values[grid[k]] = [k]
    for k in values.keys():
        if k == '.' or k == '#':
            continue
        tmp_list = list(combinations(values[k], 2))
        for pair in tmp_list:
            #res_list = find_res(pair[0], pair[1]) #part1
            res_list = p2(pair[0], pair[1], grid) #part2
            for r in res_list:
                if r in grid.keys():
                    grid[r] = '#'
                    values['#'].append(r)
    print(len(set(values['#'])))
    

            
    
if __name__ == "__main__":
    lines = read_file(filename)
    grid = make_grid(lines)
    build_it(grid)
