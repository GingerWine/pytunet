# -*- coding: utf-8 -*-

import sys
import getopt
import urllib2
import urllib
import os
from getpass import getpass
from hashlib import md5


def check():
	url = "http://net.tsinghua.edu.cn/cgi-bin/do_login"
	data = "action=check_online"
	requ = urllib2.Request(url, data)
	resp = urllib2.urlopen(requ)
	html = resp.read()
	if len(html) > 0:
		list = html.split(',')
		resp_info = str(list[1]) + ' online. '+ ' flux = ' + str(float(list[2])/1000000000) + ' GB  ' + ' time = ' + str(list[4]) + ' seconds '
		print resp_info
		return resp_info
	else:
		return 'offline'

def login(user, pwmd5):
    checkInfo = check()
    if checkInfo != 'offline':
        return (False, checkInfo)
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_login"
    login_data = "username=" + user + "&password=" + pwmd5 + "&drop=0&type=1&n=100"
    requ = urllib2.Request(url, login_data)
    resp = urllib2.urlopen(requ)
    html = resp.read()
    if html.find('error') >= 0:
        return (False, html)
    else:
        list = html.split(',')
        flux_info = 'flux = ' + str(float(list[2])/1000000000) + ' GB'
        return (True, flux_info)

def logout():
    url = "http://net.tsinghua.edu.cn/cgi-bin/do_logout"
    data = ""
    req = urllib2.Request(url, data)
    resp = urllib2.urlopen(req)
    html = resp.read()
    return html

def local(isRead, id, pw):
    dat = 'D:\tunet.dat'
    if isRead:
        if os.path.isfile(dat):
            datFile = open(dat, 'r')
            idInfo = datFile.readlines()
            userName = idInfo[0]
            pswdMD5 = idInfo[1]
            datFile.close()
            return (True, userName, pswdMD5)
        else:
            return (False, None, None)
    else:
        datFile = open(dat, 'w')
        datFile.writelines([id, pw])
        return
