#   ===================================
#               Main
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import codecs, sys, arff
from nltk.tokenize import RegexpTokenizer
import nltk.data
from encodings.utf_8 import decode

'''kanw import ths synarthseis pou exw ylopoihsei ston ypofakelo lib'''
from lib import OutPutArff, GetStr, InputFile, Izip, PercentCalc, Freq, SingleCharFreq, SlangDictionaries, WordsCount, Features


textClass = []
text = []   # lista gia to katharo keimeno
ids = []    # lista gia ta ids
temp = []
csvFile = InputFile.CSV() # anoigma to dataset csv
# to dataset me to opoio doulevw einai to sample11-extra.csv



write = codecs.open("text", "wb", "utf-8")
write_open = codecs.open("text", "rb", "utf-8")
nation = []

co = 0
# diavazw to object me to katharo keimeno
print('Dialogi ethnikotitas...')
for row in csvFile:
    # lista me to katharo keimeno
    text.append(row[1])  # pernaw sti lista text to katharo keimeno
    # lista me ta ids twn keimenwn
    ids.append(int(row[0]))  # to antistoixo id
    # lista me ta nationalities twn keimenwn

    print co,
    sys.stdout.flush()
    print "\r",
    co = co+1

freq_word = [0.0]*len(text)
del csvFile, co
print('DONE!')
print 'megethos dataset: ', len(text)

BasicFeatures = Features.Basic(len(text))

BasicCounters = Features.Counters(len(text))

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
i=[]
word = [0.0]*len(text)
print('Basic feature processing...')
for i in range(len(text)):
    print i
    # ypologismos arithmou xarakthrwn ana keimeno
    BasicFeatures['TextLen'][i]=(len(text[i]))   # lista me ton arithmo xaraktirwn
    # ypologismos toy arithmou twn symvolwn ana keimeno
    BasicCounters['Symbols'][i]=(len(RegexpTokenizer(r'[+/\-@&*{}\[\[|]').tokenize(text[i])))
    BasicFeatures['SymbolsPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Symbols'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou shmeiwn stikshs ana keimeno
    BasicCounters['Puncuations'][i]=(len(RegexpTokenizer(r'[,.?!;\'\":]').tokenize(text[i])))
    BasicFeatures['PuncuationsPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Puncuations'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn kenwn xarakthrwn ana keimeno
    BasicCounters['Spaces'][i]=(len(RegexpTokenizer(r' ').tokenize(text[i])))
    BasicFeatures['SpacesPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Spaces'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn kefalaiwn grammatwn ana keimeno
    BasicCounters['Upper'][i]=(len(RegexpTokenizer(r'[A-Z]').tokenize(text[i])))
    BasicFeatures['UpperPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Upper'][i],BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn grammatwn ana keimeno
    BasicCounters['Letters'][i]=(len(RegexpTokenizer(r'[A-Z,a-z]').tokenize(text[i])))
    BasicFeatures['LettersPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Letters'][i],BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn pshfiwn ana keimeno
    BasicCounters['Digits'][i]=(len(RegexpTokenizer(r'[0-9]').tokenize(text[i])))
    BasicFeatures['DigitsPerChar'][i]=(PercentCalc.PercentCalc(BasicCounters['Digits'][i], BasicFeatures['TextLen'][i]))
    # eisagwgh sth word twn leksewn ana keimeno
    word[i]=(RegexpTokenizer(r'\w+').tokenize(text[i]))
    # ypologismos toy arithmou twn leksewn ana keimeno
    BasicCounters['Words'][i]=(len(word[i]))
    count = 0   # metritis gia tis mikres lekseis
    StrLenCounter = 0  # metritis gia to mhkos ths kathe leksis

    for j in word[i]:

        # j = j.decode('utf8', 'replace')
        StrLenCounter += len(j)    #afkshsh toy metrith toso oso to mhkos ths lekshs
        if len(j)<4:    # elegxos an h trexousa leksi einai short
            count +=1   # an nai afkshsh toy metrith kata 1

    freq_word[i]=(nltk.FreqDist(word[i]))
    count_legomena = 0
    count_dislegomena = 0
    for j in freq_word[i]:
        if freq_word[i][j]==1:
            count_legomena+=1
        elif freq_word[i][j]==2:
            count_dislegomena+=1


    # sth lista pernaw to arithmo twn xarakthrwn pou exoun oles oi lekseis ana keimeno
    BasicFeatures['CharsINWords'][i]=(PercentCalc.PercentCalc(StrLenCounter, BasicFeatures['TextLen'][i]))

    # ypologismos toy mesou orou toy mhkous ths kathe lekshs
    BasicFeatures['AvgWordLen'][i]=(PercentCalc.PercentCalc(BasicFeatures['CharsINWords'][i],BasicCounters['Words'][i]))
    # ypologismos mesou orou protasewn ana lekseis ana keimeno
    BasicFeatures['AvgSentencesWords'][i]=(PercentCalc.PercentCalc(len(sent_detector.tokenize(text[i])),BasicFeatures['TextLen'][i]))
    # sth lista pernaw ton arithmo mikrwn leksewn kathe keimenou
    BasicFeatures['ShortWords'][i]=( PercentCalc.PercentCalc( count, BasicCounters['Words'][i] ) )
    BasicFeatures['HapaxLegomena'][i]=( PercentCalc.PercentCalc( count_legomena, BasicCounters['Words'][i] ) )
    BasicFeatures['HapaxDislegomena'][i]=( PercentCalc.PercentCalc( count_dislegomena, BasicCounters['Words'][i] ) )
    BasicFeatures['TotalDiffWords'][i]=( PercentCalc.PercentCalc( len( freq_word[i]), BasicCounters['Words'][i] ) )
    BasicFeatures['AvgSentencesChars'][i]=(float(format(len(sent_detector.tokenize(text[i]))/float(BasicFeatures['TextLen'][i]), '.3f')))

    print i,
    sys.stdout.flush()
    print "\r",
print('DONE!')


'''
    Ypologismos features gia grammata
    me xrhsh tis synarthshs LetterChars()
'''
LetterFreq = {}
LetterFreq = SingleCharFreq.LetterChars(text, BasicCounters['Letters'])

'''
    Ypologismos features gia symvola
    me xrhsh tis synarthshs SymbolChars()
'''
SymbolsFreq = {}
SymbolsFreq = SingleCharFreq.SymbolChars(text, BasicFeatures['TextLen'], BasicCounters['Symbols'])

'''
    Ypologismos features gia shmeia stiksis
    me xrhsh tis synarthshs PunctuationChars()
'''
PunctuationsFreq = {}
PunctuationsFreq = SingleCharFreq.PunctuationChars(text, BasicCounters['Puncuations'])
# leksiko sto opoio pernaw sth syxnothta emfanishs twn shmeiwn stiksews ana keimeno

# ftiaxnw to header gia to csv pou tha eksagw
header = OutPutArff.Header();

print('izip object processing...')
# me izip pernaw sto output ola ta features pou einai pros eggrafh sto csv
data = Izip.NoZipFormat(BasicFeatures, LetterFreq, SymbolsFreq, textClass, PunctuationsFreq)
print('DONE!')
print('Eggrafi arxeiou arff')
DefaultFileName = "resaults.arff"
print "Default csv file: 'resaults.arff' (Press Enter for default name)"
FileName = raw_input("Insert arff file name: ") or DefaultFileName #eisagwgh onomatos arxeiou
arff.dump(FileName, data, relation='results', names=header)
del data, header, FileName, DefaultFileName

print('DONE!')
print('TELOS - BE HAPPY :)')
