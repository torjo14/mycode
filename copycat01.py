#!/usr/bin/env python3
import shutil
import os
# The following line will create the directory if it does not exist already


os.chdir('/home/student/mycode/')
# the following line will copy a file 

shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')

# The following line copys an entire folder
shutil.copytree('5g_research/', '5g_research_backup/')

