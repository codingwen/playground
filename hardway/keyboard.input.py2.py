#! /usr/local/bin/python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import exists

# interrupting for keyboard input
print "Who are you?",
name = raw_input()

print "Where are you come from?",
where = raw_input()
print "Hello, %s of %s" %(name, where)

######################
# manipulate file  ###
######################

# command line args
script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# python keyboard.input.py2.py file1 file2