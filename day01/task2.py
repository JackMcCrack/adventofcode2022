#!/usr/bin/python3

def read_input(filename):
    num = []
    lines=open(filename, "r")
    r = -1
    for i in lines:
        for i in i.strip().split(','):
            if i == '':
                num.append('x')
            else:
                num.append(int(i))
    return num

if __name__ == '__main__':
    n = read_input("input")
    x = 0
    s = []
    for e in n:
        if e == 'x':
            s.append(x)
            x=0
        else:
            x = x + e
    s.sort(reverse=True)
    print(s)
    print(s[0:3], sum(s[0:3]))

