filename = 'day07.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def basify(num, base, pad):
    nums = []
    while num:
        num, remainder = divmod(num, base)
        nums.append(str(remainder))
    tmp = ''.join(reversed(nums))
    tmp = '0'*(pad-len(tmp))+tmp
    return tmp

def test_rule(lines):
    count = 0
    operands = ['+', '*'] #add third operand ('') for part 2
    for q, line in enumerate(lines):
        total = int(line.split(':')[0])
        nums = list(map(int, line.split(' ')[1:]))
        for k in range(len(operands)**(len(nums)-1)):
            bin = basify(k, len(operands), len(nums)-1)
            tmp_total = nums[0]
            for i in range(len(nums)-1):
                tmp_total = eval(f'{tmp_total}{operands[int(bin[i])]}{nums[i+1]}')
            if tmp_total == total:
                count += total
                break
    print(count)


    
if __name__ == "__main__":
    lines = read_file(filename)
    test_rule(lines)
    