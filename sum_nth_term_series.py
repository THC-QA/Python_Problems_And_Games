#!/usr/bin/env python3
def series_sum(n):
    s = 1
    out = 0
    for x in range(n):
        out += 1/s
        s += 3
    return round(out, 2)
print(series_sum(1))
print(series_sum(2))
print(series_sum(3))
