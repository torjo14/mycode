#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')

# Move file from one directory to another
shutil.move('raynor.obj', 'ceph_storage/')

# Change file name
xname = input('What is the new name for Kerrigan.obj?')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

