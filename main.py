#   ===================================
#               Main
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"
#   ===================================

import codecs, arff, sys
import unicodecsv as csv
from itertools import izip
from nltk.tokenize import RegexpTokenizer
import nltk.data
from encodings.utf_8 import decode

'''kanw import ths synarthseis pou exw ylopoihsei ston ypofakelo lib'''

from lib import frequencies, WordsCount, PercentCalc, GetStr, SingleCharFreq, SlangDictionaries, arff

words_count = []    # lista me ton arithmo twn leksewn ana keimeno
word = []   # lista me tis lekseis ana keimeno
spaces_count = []   # lista gia metrima twn kenwn
textClass = []

avg_sentences_chars = []  # lista gia meso oro protasewn os pros toy xarakthres
avg_sentences_words = []  # lista gia meso oro protasewn os pros tis lekseis
avg_word_len = []   # lista gia metrima toy mesou orou toy mhkous twn leksewn
letters_count = []  # lista gia to metrina twn grammatwn
letters_count_per_char = []
short_words_counter = []    # lista gia to metrima twn mikrwn leksewn (<4)
digits_count = []   # lista gia to metrima twn psifion
digits_count_per_char = []
total_chars_in_words = []   # total number of chars in word

global text
text = []   # lista gia to katharo keimeno
ids = []    # lista gia ta ids
temp = []
sample_read = csv.reader(open("sample11-2K.csv","rb")) # anoigma to dataset csv
# to dataset me to opoio doulevw einai to sample11-extra.csv

'''orisw san list ta slang gia kathe ethnikothta'''
SlangDict = { 'US': [], 'AUS' : [], 'CAN' : [], 'UK' : [], 'NNS':[] }

SlangDict['US'] = SlangDictionaries.US()

SlangDict['AUS'] = SlangDictionaries.AUS()

SlangDict['CAN'] = SlangDictionaries.CAN()

SlangDict['UK'] = SlangDictionaries.UK()

total_diff_words = []
hapax_legomena = []
hapax_dislegomena = []
freq_word = []
write = codecs.open("text", "wb", "utf-8")
write_open = codecs.open("text", "rb", "utf-8")
nation = []


text_US=[]
text_AUS=[]
text_GBR=[]
text_CAN = []
text_NNS  =[]

co = 0
# diavazw to object me to katharo keimeno
print('Dialogi ethnikotitas...')
for row in sample_read:
    # lista me to katharo keimeno
    text.append(row[1])  # pernaw sti lista text to katharo keimeno
    # lista me ta ids twn keimenwn
    ids.append(int(row[0]))  # to antistoixo id
    # lista me ta nationalities twn keimenwn
    nation.append(row[7])
    # antistoixes listes me ta keimena ana nationalities
    if row[7]=='US':
        text_US.append(row[1].encode("ascii", "ignore"))
        textClass.append(0)
    elif row[7]=='AUS':
        text_AUS.append(row[1].encode("ascii", "ignore"))
        textClass.append(1)
    elif row[7]=='CAN':
        text_CAN.append(row[1].encode("ascii", "ignore"))
        textClass.append(2)
    elif row[7]=='UK':
        text_GBR.append(row[1].encode("ascii", "ignore"))
        textClass.append(3)
    else:
        textClass.append(4)
        text_NNS.append(row[1].encode("ascii", "ignore"))
    print co,
    sys.stdout.flush()
    print "\r",
    co = co+1

FreqWordsLib = {'US':[], 'AUS': [], 'CAN': [], 'UK': [], 'NNS': []}
del sample_read, co
print('DONE!')
print 'megethos dataset: ', len(text)
print('Most used words processing...')
FreqWordsLib['US'] = frequencies.freq_words_nationality(text_US, write, write_open)
del text_US
print('US DONE!')
FreqWordsLib['AUS'] = frequencies.freq_words_nationality(text_AUS, write, write_open)
del text_AUS
print('AUS DONE!')
FreqWordsLib['CAN'] = frequencies.freq_words_nationality(text_CAN, write, write_open)
del text_CAN
print('CAN DONE!')
FreqWordsLib['UK'] = frequencies.freq_words_nationality(text_GBR, write, write_open)
del text_GBR
print('UK DONE!')
FreqWordsLib['NNS'] = frequencies.freq_words_nationality(text_NNS, write, write_open)
del text_NNS, temp
print('NNS DONE')
print('Removing commons words...')
# vriskw ta keina most commons words
commons = set(FreqWordsLib['US'])&set(FreqWordsLib['AUS'])&set(FreqWordsLib['UK'])&set(FreqWordsLib['CAN'])&set(FreqWordsLib['NNS'])
for j in commons:
    # kai ta svinw apo oles tis listes
    del FreqWordsLib['US'][j]
    del FreqWordsLib['AUS'][j]
    del FreqWordsLib['CAN'][j]
    del FreqWordsLib['UK'][j]
    del FreqWordsLib['NNS'][j]
del commons
print('DONE!')
# apo afta krataw ta 20 most commons
FreqWordsLib['US'] = FreqWordsLib['US'].most_common(50)
FreqWordsLib['AUS'] = FreqWordsLib['AUS'].most_common(50)
FreqWordsLib['CAN'] = FreqWordsLib['CAN'].most_common(50)
FreqWordsLib['UK'] = FreqWordsLib['UK'].most_common(50)
FreqWordsLib['NNS'] = FreqWordsLib['NNS'].most_common(50)

#kai apo ta antistoixa krataw mono tis lekseis xwris to value
FreqWords = {'US':[], 'AUS': [], 'CAN': [], 'UK': [], 'NNS': []}
FreqWords['US'] = GetStr.GetStrValue(FreqWordsLib['US'])
FreqWords['AUS'] = GetStr.GetStrValue(FreqWordsLib['AUS'])
FreqWords['CAN'] = GetStr.GetStrValue(FreqWordsLib['CAN'])
FreqWords['UK'] = GetStr.GetStrValue(FreqWordsLib['UK'])
FreqWords['NNS'] = GetStr.GetStrValue(FreqWordsLib['NNS'])

MostUsedWords = { 'US':[], 'AUS':[], 'CAN':[], 'UK':[], 'NNS':[] }

SlanFreq = {'US':[], 'AUS':[], 'CAN':[], 'UK':[], 'NNS':[]}

BasicFeatures = { 'TextLen':[], 'SymbolsPerChar':[], 'PuncuationsPerChar':[], 'SpacesPerChar':[],
                  'UpperPerChar':[], 'LettersPerChar':[], 'DigitsPerChar':[], 'AvgWordLen':[],
                  'AvgSentencesWords':[], 'CharsINWords':[] }

BasicCounters = { 'Symbols':[], 'Puncuations':[], 'Spaces':[], 'Upper':[], 'Letters':[],
                  'Digits':[], 'Words':[], 'ShortWords': [] }

sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
i=[]
print('Basic feature processing...')
for i in range(len(text)):
    # ypologismos arithmou xarakthrwn ana keimeno
    BasicFeatures['TextLen'].append(len(text[i]))   # lista me ton arithmo xaraktirwn
    # ypologismos toy arithmou twn symvolwn ana keimeno
    BasicCounters['Symbols'].append(len(RegexpTokenizer(r'[+/\-@&*{}\[\[|]').tokenize(text[i])))
    BasicFeatures['TextLen'].append(PercentCalc.PercentCalc(BasicCounters['Symbols'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou shmeiwn stikshs ana keimeno
    BasicCounters['Puncuations'].append(len(RegexpTokenizer(r'[,.?!;\'\":]').tokenize(text[i])))
    BasicFeatures['PuncuationsPerChar'].append(PercentCalc.PercentCalc(BasicCounters['Puncuations'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn kenwn xarakthrwn ana keimeno
    BasicCounters['Spaces'].append(len(RegexpTokenizer(r' ').tokenize(text[i])))
    BasicFeatures['SpacesPerChar'].append(PercentCalc.PercentCalc(BasicCounters['Spaces'][i], BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn kefalaiwn grammatwn ana keimeno
    BasicCounters['Upper'].append(len(RegexpTokenizer(r'[A-Z]').tokenize(text[i])))
    BasicFeatures['UpperPerChar'].append(PercentCalc.PercentCalc(BasicCounters['Upper'][i],BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn grammatwn ana keimeno
    BasicCounters['Letters'].append(len(RegexpTokenizer(r'[A-Z,a-z]').tokenize(text[i])))
    BasicFeatures['LettersPerChar'].append(PercentCalc.PercentCalc(BasicCounters['Letters'][i],BasicFeatures['TextLen'][i]))
    # ypologismos toy arithmou twn pshfiwn ana keimeno
    BasicCounters['Digits'].append(len(RegexpTokenizer(r'[0-9]').tokenize(text[i])))
    BasicFeatures['DigitsPerChar'].append(PercentCalc.PercentCalc(BasicCounters['Digits'][i], BasicFeatures['TextLen'][i]))
    # eisagwgh sth word twn leksewn ana keimeno
    word.append(RegexpTokenizer(r'\w+').tokenize(text[i]))
    # ypologismos toy arithmou twn leksewn ana keimeno
    BasicCounters['Words'].append(len(word[i]))
    count = 0   # metritis gia tis mikres lekseis
    StrLenCounter = 0  # metritis gia to mhkos ths kathe leksis

    # ypologizw ta most used words gia kathe ethnikothta
    MostUsedWords['US'].append(WordsCount.NationalCommonsPerDoc(word[i], FreqWords['US']))
    MostUsedWords['CAN'].append(WordsCount.NationalCommonsPerDoc(word[i], FreqWords['CAN']))
    MostUsedWords['UK'].append(WordsCount.NationalCommonsPerDoc(word[i], FreqWords['UK']))
    MostUsedWords['AUS'].append(WordsCount.NationalCommonsPerDoc(word[i], FreqWords['AUS']))
    MostUsedWords['NNS'].append(WordsCount.NationalCommonsPerDoc(word[i], FreqWords['NNS']))
    SlanFreq['US'].append(WordsCount.NationalCommonsPerDoc(word[i], SlanFreq['US']))
    SlanFreq['CAN'].append(WordsCount.NationalCommonsPerDoc(word[i], SlanFreq['CAN']))
    SlanFreq['AUS'].append(WordsCount.NationalCommonsPerDoc(word[i], SlanFreq['AUS']))
    SlanFreq['UK'].append(WordsCount.NationalCommonsPerDoc(word[i], SlanFreq['NNS']))
    for j in word[i]:

        # j = j.decode('utf8', 'replace')
        StrLenCounter += len(j)    #afkshsh toy metrith toso oso to mhkos ths lekshs
        if len(j)<4:    # elegxos an h trexousa leksi einai short
            count +=1   # an nai afkshsh toy metrith kata 1

    freq_word.append(nltk.FreqDist(word[i]))
    count_legomena = 0
    count_dislegomena = 0
    for j in freq_word[i]:
        if freq_word[i][j]==1:
            count_legomena+=1
        elif freq_word[i][j]==2:
            count_dislegomena+=1


    # sth lista pernaw to arithmo twn xarakthrwn pou exoun oles oi lekseis ana keimeno
    BasicFeatures['CharsINWords'].append(PercentCalc.PercentCalc(StrLenCounter, BasicFeatures['TextLen'][i]))
    if BasicCounters['Words'][i]!=0:

        # ypologismos toy mesou orou toy mhkous ths kathe lekshs
        BasicFeatures['AvgWordLen'].append(PercentCalc.PercentCalc(BasicFeatures['CharsINWords'][i],BasicCounters['Words'][i]))
        # ypologismos mesou orou protasewn ana lekseis ana keimeno
        BasicFeatures['AvgSentencesWords'].append(PercentCalc.PercentCalc(len(sent_detector.tokenize(text[i])),BasicFeatures['TextLen'][i]))
        # sth lista pernaw ton arithmo mikrwn leksewn kathe keimenou
        BasicCounters['ShortWords'].append( PercentCalc.PercentCalc( count, BasicCounters['Words'][i] ) )
        hapax_legomena.append( PercentCalc.PercentCalc( count_legomena, BasicCounters['Words'][i] ) )
        hapax_dislegomena.append( PercentCalc.PercentCalc( count_dislegomena, BasicCounters['Words'][i] ) )
        total_diff_words.append( PercentCalc.PercentCalc( len( freq_word[i]), BasicCounters['Words'][i] ) )
    else:
        #print i
        BasicFeatures['AvgWordLen'].append(0.0)
        BasicFeatures['AvgSentencesWords'].append(0.0)
        avg_sentences_words.append(0.0)
        short_words_counter.append(0.0)
        hapax_legomena.append(0.0)
        hapax_dislegomena.append(0.0)
        total_diff_words.append(0.0)
    if BasicFeatures['TextLen'][i]!=0:
        # ypologismos mesou orou protasewn ana xarakthres ana keimeno
        avg_sentences_chars.append(float(format(len(sent_detector.tokenize(text[i]))/float(BasicFeatures['TextLen'][i]), '.3f')))
    elif BasicFeatures['TextLen'][i]==0:
        print i
        avg_sentences_chars.append(0)
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
header = arff.header();

print('izip object processing...')
# me izip pernaw sto output ola ta features pou einai pros eggrafh sto csv
'''output = izip(BasicFeatures['TextLen'], BasicFeatures['SymbolsPerChar'], Puncuations_count_per_char, spaces_count_per_char,
 upper_count_per_char, letters_count_per_char, digits_count_per_char, short_words_counter, total_chars_in_words,
 avg_word_len, avg_sentences_words, avg_sentences_chars, total_diff_words, hapax_legomena, hapax_dislegomena,
LetterFreq['a'], LetterFreq['b'], LetterFreq['c'], LetterFreq['d'], LetterFreq['e'], LetterFreq['f'], LetterFreq['g'], LetterFreq['h'],
['i'], LetterFreq['j'], LetterFreq['k'], LetterFreq['l'], LetterFreq['m'], LetterFreq['n'], LetterFreq['o'], LetterFreq['p'],
['q'], LetterFreq['r'], LetterFreq['s'], LetterFreq['t'], LetterFreq['u'], LetterFreq['v'], LetterFreq['w'], LetterFreq['x'],
['y'], LetterFreq['z'], freq_symbols['@'], freq_symbols['#'], freq_symbols['$'], freq_symbols['%'],
 freq_symbols['^'], freq_symbols['&'], freq_symbols['*'], freq_symbols['-'], freq_symbols['_'], freq_symbols['='], freq_symbols['+'], freq_symbols['>'], freq_symbols['<'], freq_symbols['['], freq_symbols[']'], freq_symbols['{'], freq_symbols['}'], freq_symbols['|'], LetterFreq['p'], Puncuations[","], LetterFreq['p'],Puncuations["."], LetterFreq['p'],Puncuations["?"],
 LetterFreq['p'],Puncuations["!"], LetterFreq['p'],Puncuations[":"], LetterFreq['p'],Puncuations[";"],
 LetterFreq['p'],Puncuations["\'"], LetterFreq['p'],Puncuations["\""], MostUsedWords['US'],
 MostUsedWords['UK'], MostUsedWords['AUS'], MostUsedWords['CAN'], MostUsedWords['NNS'],
 SlanFreq['US'], SlanFreq['UK'], SlanFreq['AUS'],SlanFreq['AUS'] , stextClass)
print('DONE!')

'''
del BasicFeatures['TextLen'], textClass, BasicCounters, BasicFeatures, FreqWords, FreqWordsLib, PunctuationsFreq, StrLenCounter, SymbolsFreq
del LetterFreq, MostUsedWords, avg_sentences_chars, avg_sentences_words, freq_word, hapax_legomena, hapax_dislegomena, ids, total_diff_words, word
del SlanFreq, SlangDict, nation
'''

print('Eggrafi arxeiou arff')
arff.dump("result2.arff", output, relation='results', names=header)
del output, header
print('DONE!')
print('TELOS - BE HAPPY :)')
'''
