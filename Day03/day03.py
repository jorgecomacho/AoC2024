filename = 'day03.txt'
#filename = 'test.txt'
#filename = 'test2.txt'

import os, re

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    #lines = [i.strip() for i in f.readlines()]
    content = f.read()
    return content

def summult(lines):
    total = 0
    result = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", lines)
    for res in result:
        nums = re.findall(r"\d+", res.group())
        total += int(nums[0]) * int(nums[1])
    return total

def two(content):
    result = re.finditer(r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))", content)
    on = True
    total = 0
    for res in result:
        if res.group() == 'do()':
            on = True
            continue
        if res.group() == "don't()":
            on = False
            continue
        if on:
            nums = re.findall(r"\d+", res.group())
            total += int(nums[0]) * int(nums[1])
    return total


if __name__ == "__main__":
    lines = read_file(filename)
    print(summult(lines))
    print(two(lines))