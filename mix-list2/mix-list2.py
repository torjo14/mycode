#!/usr/bin/env python3
proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']
print(proto)

# this line will add 'dns' to the end of our list
proto.append('dns') 

# this line will add 'dns' to the end of our list
protoa.append('dns') 

print(proto)

# a list of common ports
proto2 = [ 22, 80, 443, 53 ] # a list of common ports

# pass proto2 as an argument to the extend method -- then print result
proto.extend(proto2) 

print (proto)

# pass proto2 as an argument to the append method -- then print result
protoa.append(proto2) 

print (protoa)

#my list test

protob = ['Firesat', 'Parent', 'Child', 'Open']
protoc = ['Firesat', 'Parent', 'Child', 'Open']
protod = ['Resolved', 'Closed']

print(protob)

protob.append(protod)

print(protob)

print(protoc)

protoc.extend(protod)

print(protoc)