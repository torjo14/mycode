#!/usr/bin/env python3
listl = ['cisco_nxos', 'arista_eos', 'cisco_ios']
print(listl)

#adding to the list
listl.extend(['juniper'])
print(listl)

#adding a list within the list
listl.append(['10.1.0.1', '10.2.0.1', '10.3.0.1'])
print(listl)

#shows the entire list as an item for number 4
print(listl[4])

#shows one item in the list in the list
print(listl[4][0])