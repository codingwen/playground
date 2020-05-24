#! /usr/local/bin/python
# -*- coding: utf-8 -*-

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed"
elif cats < people:
    print "Not many cats! The world is saved!"
else:
    print "nill"

fruits = ['apples', 'oranges', 'pears', 'apricots']

for fruit in fruits:
    print "A fruit of type: %s" % fruit

i = 0

while i < 6:
    print "At the top i is %d" % i

    i = i + 1

    print "At the bottom i is %d" % i