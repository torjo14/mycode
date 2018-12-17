#!/usr/bin/env python3

print("This program reserves the right to block IP addresses 10 at a time.")

round = 0
IP_addresses = []
while(True):
    round = round +1
    NewIP = input('What is the IP address, enter q to exit?:')
    IP = NewIP.split('.') 
    IP_addresses.append(IP)
    if (NewIP == 'q'):
        del IP_addresses[-1] 
        break
    elif (round == 10):
        break
IP_addresses = IP_addresses 
print('The IP addresses that will be blocked are:', IP_addresses)


