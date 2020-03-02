#!/usr/bin/env python3
# Valid Braces

def validBraces(string):
    string_list = list(string)
    discard = []
    count = 0
    removed = False
    print(string_list)
    print(len(string_list))
    if len(string_list)%2 != 0:
        return False
    while len(string_list) > 0:
        for i in range(len(string_list)):
            if string_list[i] == ")" and string_list[i+1] == "(":
                discard.append(i)
                discard.append(i+1)
                removed = True
                print(string_list)
                print(len(string_list))
                print(removed)
            elif string_list[i] == "]" and string_list[i+1] == "[":
                discard.append(i)
                discard.append(i+1)
                removed = True
            elif string_list[i] == "}" and string_list[i+1] == "{":
                discard.append(i)
                discard.append(i+1)
                removed = True
            else:
                count += 1
                print(count)
        string_list.remove(i)
        string_list.remove(i+1)
        if count == len(string_list) and removed == False:
            return False
    return True

print(validBraces("()"))
print(validBraces("[(])"))
