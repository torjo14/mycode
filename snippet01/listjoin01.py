#!/usr/bin/env python3
configfile = open('l1.txt', 'r')
a = configfile.read()
a = a.split(" ")
print(a)

print()

a = "-".join(a)
print(a)
