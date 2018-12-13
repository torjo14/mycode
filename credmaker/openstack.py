#!/usr/bin/env python3
outFile = open('admin.rc', 'a')

###########################
## Prompting user for is auth url
###########################

print('Whast is the OS_AUTH_URL?')
osAUTH = input()
print('export OS_AUTH_URL=' + osAUTH, file=outFile)
print()
print('export OS_IDENTITY_API_VERSION=3', file=outFile)

###########################
## Prompting user for os project name and write to admin file
###########################
print('\n')
print('What is the OS_PROJECT_NAME?')
osPROJ = input()
print('export OS_PROJECT_NAME=' + osPROJ, file=outFile)

###########################
## Prompting user for os project domain name
###########################
print('\n')
print('what is the OS_PROJECT_DOMAIN_NAME?')
osPROJDOM = input()
print('export OS_PROJECT_DOMAIN_NAME=' + osPROJDOM, file=outFile)

###########################
## Prompting user for os username
###########################


print('\n')
print('Whast is the OS_USERNAME?')
osUSER = input()
print('export OS_USERNAME=,' + osUSER, file=outFile)

###########################
## Prompting user for os user domain name
###########################
print('What is the OS_USER_DOMAIN_NAME?')
osUSERDOM = input()
print('export OS_USER_DOMAIN_NAME=' + osUSERDOM, file=outFile)

###########################
## Prompting user for os PW
###########################
print('what is the OS_PASSWORD?')
osPASS = input()
print('export OS_PASSWORD=' + osPASS, file=outFile)

outFile.close()







