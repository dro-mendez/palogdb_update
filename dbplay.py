#!/usr/bin/python

'''''
stuff on db amd python

'''''


import MySQLdb
import optparse
import getpass
import string

mydb = MySQLdb.connect(host='192.168.56.103',
    user='emendez',
    passwd='welcome123',
    db='palogdb')
cursor = mydb.cursor()


