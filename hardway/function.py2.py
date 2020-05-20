#! /usr/local/bin/python
# -*- coding: utf-8 -*-

def add(a, b):
    """Do add calculation"""
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracing %d - %d" % (a, b)
    return a - b

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)

print "Age: %d, Height: %d" % (age, height)

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)