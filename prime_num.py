#!/usr/bin/env python3
def prime_num(lower,upper):
    num_list=[]
    for n in range(lower,upper):
        is_prime = True
        for d in range(2,int(n/2)):
            if n%d == 0:
                is_prime = False
        if is_prime:
            num_list.append(n)
    return num_list
print(prime_num(1000,3000))