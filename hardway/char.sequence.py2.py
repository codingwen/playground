#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# 关于字符和字符串的用法几乎都在这里了
print "Hello World!"
print 'Hello Again'
print "I'd much rather you 'not', or \"not\""
print 'I "said" do not touch this, notice the word \'said\''

print "They are John", "Jack", "Philip"
print "What is 3 + 2?", 3 + 2
print "This is first line.",
print "This should be second line, but the end of upper line there is a comma, so"

print "." * 20 # what did this do?

my_name = 'Zed A. Shaw'
my_height = '6\'2'
my_weight = 180 # lbs

print "He's", my_height, "inches tall and ", my_weight, "pounds."
print "He's name is %s" % my_name
print "He's %s inches tall and %d pounds." % (my_height, my_weight)

str1 = "He's name is %s" 
str2 = "He's %s inches tall and %d pounds."
print (str1 + str2) % (my_name, my_height, my_weight)
print str1 % my_name + "\n" + str2 % (my_height, my_weight)

print "." * 20 # gap line

formatter = "%r %r"
print formatter % (1,2)
print formatter % ("one", "two")
print formatter % (
    "I got this,",
    "I mean it."
)

print "." * 20 # gap line

print """
There's something going on here.
With the three double-quotes.
"""