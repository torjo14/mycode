#!/usr/bin/env python3

x = int(input("Enter a number: "))

f=1

##################################################################
# the change here was to make x into x+1
# the range is not inclusive of the final number so would need x+1
##################################################################

for i in range(1,x+1): 
	f = f*i

print(str(x) + '! = ' + str(f))
