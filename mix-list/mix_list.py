#!/usr/bin/env python3

####creating list my_list####
my_list = ["192.168.0.5", 5060, "UP" ]

### printing items on the list####
print("This is the first item in the list (IP): " +my_list[0] )

#### using string becuase vaule is an intiger###
print("The second item on the list (port): "+str(my_list[1]))
print("The last item in the list (state): " +my_list[2] )

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

####printing new list info###
print("When I " + new_list[5] + " into IP address " +new_list[3] + "or " +new_list[4] ,"I am unable to ping ports " + str(new_list[0]) + "," +new_list[1] + "," + str(new_list[2]))