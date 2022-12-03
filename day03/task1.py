#!/usr/bin/python3

def read_input(filename):
    num = []
    lines=open(filename, "r")
    r = -1
    for i in lines:
        i = i.strip()
        c = int(len(i)/2)
        a = i[0:c]
        b = i[c:len(i)]
        num.append([a,b])
    return num

if __name__ == '__main__':
    n = read_input("input")
    r = 0
    s = []
    for a,b in n:
        for x in set(a):
            # print(x, a.count(x), b.count(x))
            if a.count(x) >= 1 and b.count(x) >= 1:
                #print(x, ord('A')-27, ord('Z')-52,ord('a')-1,ord('z')-26)
                if x.islower():
                    r = r + ord(x)-96
                else:
                    r = r + ord(x)-38
        print(r)

