import codecs

def GetStrValue(DictList):
    ValueList = []
    for i, j in DictList:
        ValueList.append(i.encode("ascii","ignore"))
    del DictList
    print(ValueList)
    return ValueList
