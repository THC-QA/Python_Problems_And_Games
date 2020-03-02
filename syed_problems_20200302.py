#!/usr/bin/env python3
def multChar(x):
    x = list(x)
    out = ""
    for ch in x:
        out += ch*3
    return out
print(multChar("The"))
print(multChar("AAbb"))
print(multChar("Hi-There"))
def getBert(x):
    x = x.lower().split("bert")
    out = ""
    if len(x) == 3:
        x = x[1]
        out += x[::-1]
    return out
print(getBert("bertclivebert"))
print(getBert("xxbertfridgebertyy"))
print(getBert("xxBertfridgebERtyy"))
print(getBert("xxbertyy"))
print(getBert("xxbeRTyy"))
def evenlySpaced(a,b,c):
    numlist = [a,b,c]
    numlist.sort()
    if abs(numlist[0]-numlist[1]) == abs(numlist[1]-numlist[2]):
        return True
    return False
print(evenlySpaced(2,4,6))
print(evenlySpaced(4,6,2))
print(evenlySpaced(4,6,3))
print(evenlySpaced(4,60,9))
def nMid(string, a):
    return string[:int(((len(string)-a)/2))] + string[int(-(((len(string)-a)/2))):]
print(nMid("Hello",3))
print(nMid("Chocolate",3))
print(nMid("Chocolate",1))