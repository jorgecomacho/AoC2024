filename = 'day06.txt'
#filename = 'test.txt'

import os
import copy


def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines


def pathify(lines):
    directions = {'^':(-1, 0), 'v':(1, 0), '<':(0,-1), '>':(0, 1)}
    turn = {'^':'>', '>':'v', 'v':'<', '<':'^'}
    grid = []
    for line in lines:
        grid.append([c for c in line])
    guard = [-1, -1]
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c in directions.keys():
                guard = [i, j]
                break
        if guard != [-1,-1]:
            break
    current_dir = grid[guard[0]][guard[1]]
    next = [0,0]
    while True:
        next = [guard[0]+directions[current_dir][0], guard[1]+directions[current_dir][1]]
        if not 0 <= next[0] < len(lines) or not 0 <= next[1] < len(lines[0]):
            break
        if grid[next[0]][next[1]] != '#':
            guard = next
            grid[next[0]][next[1]] = 'X'
            continue
        current_dir = turn[current_dir]
    count = 0
    for line in grid:
        count += line.count('X')
    print(count)


def idk(lines):
    directions = {'^':(-1, 0), 'v':(1, 0), '<':(0,-1), '>':(0, 1)}
    turn = {'^':'>', '>':'v', 'v':'<', '<':'^'}
    grid = []
    guard = [-1,-1]
    for line in lines:
        grid.append([[c,''] for c in line])
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            if c[0] in directions.keys():
                grid[i][j][1] = c[0]
                guard = [i, j]
    count = 0
    for i, line in enumerate(grid):
        for j, c in enumerate(line):
            #print(i, j)
            tmp_grid = copy.deepcopy(grid)
            if tmp_grid[i][j][0] == '#' or tmp_grid[i][j][0] in directions.keys():
                continue
            tmp_grid[i][j][0] = '#'
            tmp_guard = copy.deepcopy(guard)
            current_dir = grid[guard[0]][guard[1]][0]
            limit = 0
            while True:
                '''limit += 1
                if limit > 100000:
                    count += 1
                    break'''
                next = [tmp_guard[0]+directions[current_dir][0], tmp_guard[1]+directions[current_dir][1]]
                if not 0 <= next[0] < len(lines) or not 0 <= next[1] < len(lines[0]):
                    break
                if tmp_grid[next[0]][next[1]] == ['X',current_dir]:
                    count+=1
                    break
                if tmp_grid[next[0]][next[1]][0] != '#':
                    tmp_grid[tmp_guard[0]][tmp_guard[1]] = ['X', current_dir]
                    tmp_guard = next[:]
                    continue
                current_dir = turn[current_dir]
    print(count)





if __name__ == "__main__":
    lines = read_file(filename)
    #pathify(lines)
    idk(lines)
    