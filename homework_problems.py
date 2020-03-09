#!/usr/bin/env python3
def largest(string):
    out = []
    string = string.split()
    for n in string:
        int_n = []
        for char in n:
            int_n.append(int(char))
        out.append(sum(int_n))
    return max(out)
def compares(string, num, char):
    if len(string) < num:
        return False
    elif string[num-1] == char:
        return True
    return False
def return_position(string, char):
    string = string.split()
    string = "".join(string)
    for ch in string:
        if ch == char:
            return string.index(ch) + 1
    return -1
def superBlock(string):
    letters_dict = { i:0 for i in list(set(string))}
    l = len(string)
    for i in range(l):
        cur_count = 1
        for j in range(i+1,l):
            if (string[i] != string[j]):
                break
            cur_count += 1
        if cur_count > count:
            count = cur_count
    return count
def amISearch(string):
    string = string.split()
    count = 0
    for i in string:
        if i.lower() == "am":
            count += 1
    return count