#!/usr/bin/python3

def read_input(filename):
    num = []
    t = []
    lines=open(filename, "r")
    for i in lines:
        t.append(i.strip())
    j = 0
    while len(t) > j:
        num.append(t[j:j+3])
        j = j + 3
    return num

if __name__ == '__main__':
    n = read_input("input")
    r = 0
    s = []
    for a,b,c in n:
        for x in set(a):
            if a.count(x) >= 1 and b.count(x) >= 1 and c.count(x) >=1:
                if x.islower():
                    r = r + ord(x)-96
                else:
                    r = r + ord(x)-38
        print(r)

