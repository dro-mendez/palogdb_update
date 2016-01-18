'''
example of csv import
'''

import csv

#with open ('/Users/alex/Downloads/GVV_TEST.csv', 'rb') as f:
with open ('/Users/alex/Downloads/PALOG_DEMODATA.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        print row


