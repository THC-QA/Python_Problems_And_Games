#!/usr/bin/env python3
# number string sorter

def order(sentence):
  char_list = [ch for ch in sentence]
  num_list = []
  for ch in char_list:
      if ch.isnumeric():
          num_list += [int(ch)]
  sorted_list = sorted(num_list)
  out = ""
  count = 0
  for ch in char_list:
      if ch.isnumeric():
          out += str(sorted_list[count])
          count += 1
      else:
          out += ch
  return out
print(order("is2 Thi1s T4est 3a"))