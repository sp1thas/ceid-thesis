#   ===================================
#           GetStr
#   ===================================

__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

import codecs

def Value(DictList):
    ValueList = []
    for i, j in DictList:
        ValueList.append(i.encode("ascii","ignore"))
    del DictList
    print(ValueList)
    return ValueList
