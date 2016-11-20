# -*- coding: utf-8 -*-
import unicodecsv as csv

DefaultFile = "out2.csv"
print "Default csv file: '50docs.csv' (Press Enter for default csv file)"
csvFile = raw_input("Insert csv file name: ") or DefaultFile #eisagwgh onomatos arxeiou

textFile = csv.reader(open(csvFile,"rb")) # anoigma to dataset csv
counter = 0
Male_Authors = 0
Female_Authors = 0
Facebook_Authors = 0
Twitter_Authors = 0
for row in textFile:
    if counter == 0:
        tmp = row
        counter += 1
        Authors = 1
    elif tmp[2]!=row[2] or tmp[3]!=row[3] or tmp[4]!=row[4] or tmp[5] != row[5] or tmp[6] != row[6] or tmp[7] != row[7]:
        counter += 1
        Authors += 1
        if tmp[2]=='M':
            Male_Authors += 1
        else:
            Female_Authors += 1
        if tmp[5] == 'Facebook':
            Facebook_Authors += 1
        if tmp[5] == 'Twitter':
            Twitter_Authors += 1
        tmp = row
print 'Authors: ',Authors
print 'Male Authors: ', Male_Authors
print 'Female Authors: ', Female_Authors
print 'Facebook Authors: ', Facebook_Authors
print 'Twitter Authors: ', Twitter_Authors
