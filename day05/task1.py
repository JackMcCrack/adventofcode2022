#!/usr/bin/python3

def read_input(filename):
    stack = []
    moves = []
    for x in range(9):
        stack.append([])
    lines=open(filename, "r")
    for l in lines:
        if '[' in l:
            x = 1
            y = 0
            while x <= len(l):
                if l[x] != ' ':
                    stack[y].insert(0, l[x])
                x = x + 4
                y = y + 1
        if l[0:4] == 'move':
            x = l.strip().split(' ')
            moves.append([int(x[1]),int(x[3])-1,int(x[5])-1])

    return stack, moves

if __name__ == '__main__':
    s,moves = read_input("input")
    for x, f, t in moves:
        while x > 0:
            x = x - 1
            s[t].append(s[f].pop())
    for x in range(9):
        y = ""
        if len(s[x]) > 0:
            print(s[x][len(s[x])-1])
