'''

opens log file
greps data for date range and puts into temp csv file
opens csv file
inserts each row of data data into MySQL database

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

    cursor.execute('INSERT INTO palogdb(RECEIVE_TIME, \
SERIAL, \
,TYPE \
,SUBTYPE \
,COL1	\
,TIME_GENERATED	\
,SRC	\
,DST	\
,NATSRC	\
,NATDST	\
,RULE	\
,SRCUSR	\
,DSTUSR	\
,APP	\
,VSYS1	\
,FROM	\
,TO	\
,INBOUND_IF	\
,OUTBOUND_IF	\
,LOGSET	\
,COL2	\
,SESSIONID	\
,COL3	\
,REPEATCNT	\
,SOURCEPORT	\
,NATSPORT	\
,NATDPORT	\
,FLAGS	\
,PROTO	\
,ACTION	\
,BYTES	\
,BYTES_SENT	\
,BYTES_RECEIVED	\
,PACKETS	\
,START	\
,ELAPSED	\
,CATEGORY	\
,COL4	\
,SEQNO	\
,ACTIONFLAGS	\
,SRCLOC	\
,DSTLOC	\
,NONE	\
,PKTS_SENT	\
,PKTS_RECEIVED	\
,SESSION_END_REASON)' \
          'VALUES("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", \
          "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", \
          "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", \
          "%s", "%s", "%s", "%s", "%s", "%s")')
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"