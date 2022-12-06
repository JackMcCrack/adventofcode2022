#!/usr/bin/python3

def read_input(filename):
    data = []
    lines=open(filename, "r")
    for l in lines:
        l.strip()
        data.append(l)
    return data

if __name__ == '__main__':
    d = read_input("input")
    unique_char = 4
    for l in d:
        x = 0
        while x+unique_char < len(l):
            check = (l[x:x+unique_char])
            if len(set(check)) == unique_char:
                print(x+unique_char)
                break
            x = x + 1
