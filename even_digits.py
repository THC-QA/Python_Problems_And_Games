#!/usr/bin/env python3
def span_even():
    out = []
    for i in range(1000,3000):
        i = [int(x) for x in str(i)]
        n = []
        for ch in i:
            if ch%2 == 0:
                n.append(ch)
        if len(n) == len(i):
            l = ""
            for ch in i:
                l+=str(ch)
            out.append(int(l))
    return out
print(span_even())