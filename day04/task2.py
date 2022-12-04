#!/usr/bin/python3

def read_input(filename):
    num = []
    lines=open(filename, "r")
    for l in lines:
        a,b = l.strip().split(',')
        a = a.split('-')
        b = b.split('-')
        a = [int(a[0]),int(a[1])]
        b = [int(b[0]),int(b[1])]
        num.append([a,b])
    return num

if __name__ == '__main__':
    n = read_input("input")
    x = 0
    for a,b in n:
        if not (a[0] < b[0] and a[1] < b[0] or a[0] > b[1] and a[1] > b[1]):
            x = x + 1
    print(x)
