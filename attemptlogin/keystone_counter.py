#!/usr/bin/env python3

#### Counter set to 0
loginfail = 0
logingo = 0
iplist = []

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')

keystone_file_lines=keystone_file.readlines()

for i in range(len(keystone_file_lines)):
	if"Authorization failed" in keystone_file_lines[i]:
		loginfail += 1 # This is the same as loginfail = loginfail+1
		tline = keystone_file_lines[i]
		temp,ipaddress = tline.split('from')
		iplist.append(ipaddress)
	else:
		logingo += 1 # This is the same as logingo = logingo+1	
print('The number of successful log in attempts is ' + str(logingo))
print('The number of failed log in attempts is ' + str(loginfail))
for x in iplist:
	print('The failed attempts came from IP adress:', x, end="")

