# -*- coding: UTF-8 -*-
'''
Created on 2016年3月1日

@author: yupeng
'''
import os;
import time;
# 1. The files and directories to be backed up are specified in a list.
source = ['/Users/yupeng/backup']
# If you are using Windows, use source = [r'C:\Documents', r'D:\Work'] or something like that

# 2. The backup must be stored in a main backup directory
target_dir = '/Users/yupeng/backup2/'
# 3. The files are backed up into a zip file.
# 4. The name of the zip archive is the current date and time
target = target_dir +time.strftime('%Y%m%d%H%M%S')+'.zip'
# 5. We use the zip command (in Unix/Linux) to put the files in a zip archive
zip_command = "zip -qr '%s' %s" % (target, ''.join(source))
if os.system(zip_command) == 0:
    print 'Successful backup to' , target
else:
    print 'Backup Failed'