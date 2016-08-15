#   ===================================
#              InputFile
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

'''
    script me to opoio epilegete to csv arxeio eisodou
'''
import unicodecsv as csv

def CSV():
    DefaultFile = "concession_contrariness_1.csv"
    print "Default csv file: 'concession_contrariness_1.csv' (Press Enter for default csv file)"
    csvFile = raw_input("Insert csv file name: ") or DefaultFile #eisagwgh onomatos arxeiou
    return csv.reader(open(csvFile,"rb")) # anoigma to dataset csv
