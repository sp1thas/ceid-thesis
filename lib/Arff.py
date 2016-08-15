#   ===================================
#           arff
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

'''
    me th synarthsh header() dhmiourgoume
    ta label twn xarakthristikw sto
    arxeio arff
'''
#   ===================================
import arff

def header():
    return [ 'SymbolsPerChar',
             'PunctuationsPerChar',
             'SpacesPerChar',
             'UppersPerChar',
             'LettersPerChar',
             'DigitsPerChar',
             'SortWordsPerChar',
             'TotalCharsInWords',
             'AvgWordLength',
             'AvgSentencesPerWord',
             'AvgSentencesPerChar',
             'TotalDifferentWordsPerWords',
             'HapaxLegomenaPerWords',
             'HapaxDislegomenaPerWords',
             'FreqA',
             'FreqB',
             'FreqC',
             'FreqD',
             'FreqE',
             'FreqF',
             'FreqG',
             'FreqH',
             'FreqI',
             'FreqJ',
             'FreqK',
             'FreqL',
             'FreqM',
             'FreqN',
             'FreqO',
             'FreqP',
             'FreqQ',
             'FreqR',
             'FreqS',
             'FreqT',
             'FreqV',
             'FreqU',
             'FreqW',
             'FreqX',
             'FreqY',
             'FreqZ',
             'FreqSmblTilde',
             'FreqSmblAt',
             'FreqSmblHash',
             'FreqSmblDollar',
             'FreqSmblPercent',
             'FreqSmblCaret',
             'FreqSmblAmpersand',
             'FreqSmblAsterisk',
             'FreqSmblDash',
             'FreqSmblDash1',
             'FreqSmblEqulsSign',
             'FreqSmblPlus',
             'FreqSmblGreater',
             'FreqSmblLess',
             'FreqPunctBracket1',
             'FreqPunctBracket2',
             'FreqPunctBracket3',
             'FreqPunctBracket4',
             'FreqPunctVerticalBar',
             'FreqPunctComma',
             'FreqPunctFullStop',
             'FreqPunctQuestionMark',
             'FreqPunctExclamationMark',
             'FreqPunctColon',
             'FreqPunctSemiColon',
             'FreqPunctQuotationMark1',
             'FreqPunctQuotationMark2',
             'MostUsedWrdsUS',
             'MostUsedWrdsUK',
             'MostUsedWrdsAUS',
             'MostUsedWrdsCAN',
             'MostUsedWrdsNNS',
             'FreqWrdsUS',
             'FreqWrdsUK',
             'FreqWrdsAUS',
             'FreqWrdsCAN',
             'class'
            ]
def Write(header,data):
    print('Eggrafi arxeiou arff')
    DefaultFileName = "resaults.arff"
    print "Default csv file: 'resaults.arff' (Press Enter for default name)"
    FileName = raw_input("Insert arff file name: ") or DefaultFileName #eisagwgh onomatos arxeiou
    arff.dump(FileName, data, relation='results', names=header)
    del data, header, FileName, DefaultFileName
