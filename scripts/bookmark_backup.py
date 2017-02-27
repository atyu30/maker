#!/usr/bin/env python
# encoding: utf-8

# author: Atyu30 <ipostfix (at) gmail.com>
# filename: bookmark_backup.py
# version: 2017-02-14 14:07
# copyrigth:  http://www.atyu30.com/
# description: 
#
import getpass
import os
import time
import ConfigParser
import platform

'''
Firefox
Mac: ~/Library/Application\ Support/Firefox
Red Hat: ~/.mozilla/firefox/

Chrome
Mac: ~/Library/Application\ Support/Google/Chrome/Default/Bookmarks
Red Hat: ~/.config/google-chrome/Default
'''

class Browser():
    def __init__(self):
        '''获取当前用户'''
        self.home = os.path.expanduser('~')


    def testplatform(self):
        #获取操作系统名称及版本号
        sysstr = platform.platform()  
        if "Windows" in sysstr:
            print ("Call Windows tasks")
            firefox_directories = ''
            chrome_directories = ''
            return firefox_directories, chrome_directories
        elif "Linux" in sysstr:
            firefox_directories = self.home + os.sep + ".mozilla/firefox/"
            chrome_directories = self.home + os.sep + ".config/google-chrome/Default"
            print ("Call RHEL tasks")
            return firefox_directories, chrome_directories
        elif "Darwin" in sysstr:
            firefox_directories = self.home + os.sep + "Library/Application Support/Firefox"
            chrome_directories = self.home + os.sep + "Library/Application Support/Google/Chrome/Default/Bookmarks"
            print ("Call MAC tasks")
            return firefox_directories, chrome_directories
        elif "OpenBSD" in sysstr:
            firefox_directories = ''
            chrome_directories = ''
            print ("Call OpenBSD tasks")
            return firefox_directories, chrome_directories
        else:
            firefox_directories = ''
            chrome_directories = ''
            print ("Other System tasks")
            return firefox_directories, chrome_directories

    def firefox_check(self):
        firefox_path = self.testplatform()[0]
        firefox_home_config = firefox_path + os.sep + "profiles.ini"
        config = ConfigParser.ConfigParser()
        config.readfp(open(firefox_home_config))
        firefox_home = config.get("Profile0","Path")
        firefox_bookmark = firefox_path +os.sep + firefox_home + os.sep + "places.sqlite"
        '''检查文件是否存在'''
        if not os.path.isfile(firefox_bookmark) :
            print 'Firefox favorite not found', firefox_bookmark
            firefox_bookmark = ''

        return firefox_bookmark

    def chrome_check(self):
        chrome_bookmark = self.testplatform()[1]
        '''检查文件是否存在'''
        if not os.path.isfile(chrome_bookmark) :
            print 'Chrome favorite not found', chrome_bookmark
            chrome_bookmark = ''
        return chrome_bookmark

    def backup_bookmark(self):
        firefox_bookmark = self.firefox_check()
        chrome_bookmark = self.chrome_check()
        # 判断 Firefox,Chrome 是否真实存在
        source = [ firefox_bookmark, chrome_bookmark ]
        while '' in source:
            source.remove('')

        if source:
            target_dir = '/opt/backup/favorite/'

            today = target_dir + time.strftime('%Y%m%d')
            now = time.strftime('%H%M%S')

            '''检查备份目录是否存在'''
            if not os.path.exists(target_dir) :
                os.makedirs(target_dir)
                print 'Successfully created directory', target_dir

            if not os.path.exists(today) :
                os.mkdir(today)
                print 'Successfully created directory', today

            target = today + os.sep + now + '.zip'
            zip_command = "zip -qr \"%s\" \"%s\"" % (target, '\" \"'.join(source))
            #zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

            if os.system(zip_command) == 0 :
                print 'Sucessful backup to', target
            else:
                print 'Backup FAILED'

        else:
            print "where is your browser?"

    def export_bookmark(self):
        pass


if __name__ == '__main__':
    b = Browser()
    b.backup_bookmark()
