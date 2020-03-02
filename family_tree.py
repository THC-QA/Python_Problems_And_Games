#!/usr/bin/env python3
# Family tree generator
from random import randint
from custom_functions import san_input
class member:
    def __init__(self, name = san_input("Input member first name: ", "alpha_word"), surname = None):
        self.name = name
        self.id = str(randint(0,999)) + str(name)
        self.info = {}
        self.parents = {"Father":"","Mother":""}
        if surname == None:
            if self.parents["Father"] != "":
                father_surname = self.parents[Father].split()
                surname = father_surname[len(father_surname)-1]
        self.surname = surname
        self.spouse = []
        self.children = []
    def __repr__(self):
        return self.name
    def dump(self):
        info = ""
        for st in self.info:
            info += st
            info += ": "
            info += str(self.info[st])
            info += ", "
        parents = ""
        for st in self.parents:
            parents += st
            parents += ": "
            parents += str(self.parents[st])
            info += ", "
        return "Person: {} {}\n {}\n {}\n Spouse: {}\n Children: {}".format(self.name, self.surname, info[:(len(info)-3)], parents, self.spouse[(len(self.spouse)-1):], str(self.children))
    def add_info_gender(self, gender = input("Input " + self.name + " gender: ")):
        self.info["Gender"] = gender
    def add_info_age(self, age = san_input("Input " + self.name + " age: ", "int")):
        self.info["Age"] = age
    def marriage(self, spouse):
        self.spouse += [spouse.name]
        spouse.spouse += [self.name]
    def birth(self, child):
        self.children += [child.name]
        if self.info["Gender"].startswith("m" or "M") == True:
            child.parents["Father"] = str(self.name) + ' ' + str(self.surname) + ' '
        elif self.info["Gender"].startswith("f" or "F") == True:
            child.parents["Mother"] = str(self.name) + " " + str(self.surname) + ' '
        else:
            child.parents["Parent"] = str(self.name) + " " + str(self.surname) + ' '

a = member("Dave", "Jenkins")
a.add_info_gender()
a.add_info_age()
b = member("Suzy", "Ulster")
b.add_info_gender()
b.add_info_age()
a.marriage(b)
c = member("Jimbob")
b.birth(c)

print(a.dump())
print(b.dump())
print(c.dump())