filename = 'day04.txt'
#filename = 'test.txt'

import os

def read_file(fname):
    directory = os.path.dirname(os.path.realpath(__file__))
    full_path = '/'.join([directory, fname])
    f = open(full_path,"r")
    lines = [i.strip() for i in f.readlines()]
    return lines

def oof(lines):
    count = 0
    word = 'XMAS'
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == word[0]:
                try:
                    if word == line[j:j-len(word):-1]:   #left
                        count+=1
                        #print('left', f"{i},{j}")
                except:
                    pass
                try:
                    if word == line[j:j+len(word)]:   #right
                        count+=1
                        #print('right', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i-k][j]
                    if word == tmp:   #up
                        count+=1
                        #print('up', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i+k][j]
                    if word == tmp:   #down
                        count+=1
                        #print('down', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i-k][j-k]
                    if word == tmp:   #upleft
                        count+=1
                        #print('upleft', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i-k][j+k]
                    if word == tmp:   #upright
                        count+=1
                        #print('upright', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i+k][j-k]
                    if word == tmp:   #downleft
                        count+=1
                        #print('downleft', f"{i},{j}")
                except:
                    pass
                try:
                    tmp = ''
                    for k in range(len(word)):
                        tmp += lines[i+k][j+k]
                    if word == tmp:   #downright
                        count+=1
                        #print('downright', f"{i},{j}")
                except:
                    pass
    return count

def double_oof(lines):
    count = 0
    word = 'MAS'
    
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            t1 = False
            t2 = False
            if c != 'M' and c != 'S':
                continue
            try:
                tmp = ''
                for k in range(len(word)):
                    tmp += lines[i+len(word)-1-k][j+len(word)-1-k]
                if word == tmp:   #upleft
                    t1 = True
                    print('upleft', f"{i},{j}")
            except:
                pass
            try:
                tmp = ''
                for k in range(len(word)):
                    tmp += lines[i+len(word)-1-k][j+k]
                if word == tmp:   #upright
                    t2 = True
                    print('upright', f"{i},{j}")
            except:
                pass
            try:
                tmp = ''
                for k in range(len(word)):
                    tmp += lines[i+k][j+len(word)-1-k]
                if word == tmp:   #downleft
                    t2 = True
                    print('downleft', f"{i},{j}")
            except:
                pass
            try:
                tmp = ''
                for k in range(len(word)):
                    tmp += lines[i+k][j+k]
                if word == tmp:   #downright
                    t1 = True
                    print('downright', f"{i},{j}")
            except:
                pass
            print(t1, t2)
            if t1 and t2:
                print(i, j)
                count += 1
    return count
    
if __name__ == "__main__":
    lines = read_file(filename)
    newlist = ['4' * (len(lines[0])+2)]
    for line in lines:
        newlist.append('4'+line+'4')
    newlist.append('4' * (len(lines[0])+2))
    print(oof(newlist))
    print(double_oof(newlist))