#!/usr/bin/python

'''

opens logfile/csv file
inserts range of columns from  csv file to database

'''

import csv
import MySQLdb

mydb = MySQLdb.connect(host='192.168.56.103',
    user='emendez',
    passwd='welcome123',
    db='palogdb')
cursor = mydb.cursor()

csv_data = csv.reader(file('/Users/alex/Downloads/PALOG_DEMODATA.csv'))
for row in csv_data:
        #print(row)
        cursor.execute('INSERT INTO traffic(RECEIVE_TIME,SERIAL,TYPE,SUBTYPE,COL1,TIME_GENERATED,SRC,DST,NATSRC,NATDST,RULE,SRCUSR,DSTUSR,APP,VSYS1, \
        SFROM,DTO,INBOUND_IF,OUTBOUND_IF,LOGSET,COL2,SESSIONID,COL3,REPEATCNT,SOURCEPORT,NATSPORT,NATDPORT,FLAGS,PROTO,ACTION,BYTES,BYTES_SENT,\
        BYTES_RECEIVED,PACKETS,START,ELAPSED,CATEGORY,COL4,SEQNO,ACTIONFLAGS,SRCLOC,DSTLOC,NONE,PKTS_SENT,PKTS_RECEIVED,SESSION_END_REASON) \
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',row)
#close the connection to the database.

# testing mysql injection
#cursor.execute('INSERT INTO traffic(RECEIVE_TIME) values("13:33:47")')
cursor.close()

#print "Done"