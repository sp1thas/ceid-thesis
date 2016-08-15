#   ===================================
#           SingleCharFreq
#   ===================================

__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

'''
    Synartisi gia ton ypologismo twn features gia ta shmeia stiksh
    pernei ws orisma to text kai epistrefei ena dictionary me tis
    metriseis gia kathe ena shmeio stiksis
'''

import PercentCalc, sys
from nltk.tokenize import RegexpTokenizer

def PunctuationChars(TextCorpus, PunctCounter):
    length = len(TextCorpus)
    FreqDict =  {
                        '1':[0.0]*length, '2':[0.0]*length, '3':[0.0]*length, '4':[0.0]*length,
                        '5':[0.0]*length, '6':[0.0]*length, '7':[0.0]*length, '8':[0.0]*length
                }
    print('Puncuations frequency processing...')
    for punct in range(len(TextCorpus)):
        if PunctCounter[punct] > 0 :  # ypologismos syxnothtas emfanhshs shmeiwn stiksews ana keimeno
            FreqDict['1'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[,]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['2'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[.]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['3'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[?]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['4'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[!]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['5'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[:]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['6'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[;]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['7'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\']').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['8'][punct]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\"]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
        print punct,
        sys.stdout.flush()
        print "\r",
    print('Done')
    return FreqDict
    del FreqDict, TextCorpus, punct, PunctCounter, length



'''
    Synartisi gia ton ypologismo twn features gia ta symvola
    pernei ws orisma to text kai epistrefei ena dictionary me tis
    metriseis gia kathe ena symvolo
'''
def SymbolChars(TextCorpus, TextLen, SymbolsCounter):
    length = len(TextCorpus)
    print('Symbols frequency processing...')
    SymbolDict = {
                    '1':[0.0]*length, '2':[0.0]*length, '3':[0.0]*length, '4':[0.0]*length,
                    '5':[0.0]*length, '6':[0.0]*length, '7':[0.0]*length, '8':[0.0]*length,
                    '9':[0.0]*length, '10':[0.0]*length, '11':[0.0]*length, '12':[0.0]*length,
                    '13':[0.0]*length, '14':[0.0]*length, '15':[0.0]*length, '16':[0.0]*length,
                    '17':[0.0]*length, '18':[0.0]*length, '19':[0.0]*length, '20':[0.0]*length,
                    '21':[0.0]*length
                 }
    for symbol in range(len(TextCorpus)):     # an sto keimeno den emfanizetai kanena
        if TextLen!=0:  # ypologismos syxnothtas emfanishs symvolwn ana keimeno
            SymbolDict['1'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[~]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['2'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[@]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['3'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[#]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['4'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[$]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['5'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[%]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['6'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\^]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['7'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[&]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['8'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[*]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['9'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[-]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['10'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[_]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['11'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[=]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['12'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[+]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['13'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[<]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['14'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[>]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['15'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[{]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['16'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[}]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['17'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[[]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['18'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\]]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['19'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[/]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['20'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r"['\']").tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['21'][symbol]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[|]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
        print symbol,
        sys.stdout.flush()
        print "\r",
    print('Done')
    return SymbolDict
    del SymbolDict, symbol, TextCorpus, TextLen, SymbolsCounter

'''
    Synartisi gia ton ypologismo twn features gia ta grammata
    pernei ws orisma to text kai epistrefei ena dictionary me tis
    metriseis gia kathe ena gramma
'''
def LetterChars(TextCorpus, LettersCounter):
    length = len(TextCorpus)
    LetterDict = {  'a':[0.0]*length, 'b':[0.0]*length, 'c':[0.0]*length, 'd':[0.0]*length,
                    'e':[0.0]*length, 'f':[0.0]*length, 'g':[0.0]*length, 'h':[0.0]*length,
                    'i':[0.0]*length, 'j':[0.0]*length, 'k':[0.0]*length, 'l':[0.0]*length,
                    'm':[0.0]*length, 'n':[0.0]*length, 'o':[0.0]*length, 'p':[0.0]*length,
                    'q':[0.0]*length, 'r':[0.0]*length, 's':[0.0]*length, 't':[0.0]*length,
                    'u':[0.0]*length, 'v':[0.0]*length, 'w':[0.0]*length, 'x':[0.0]*length,
                    'y':[0.0]*length, 'z':[0.0]*length }

    for letter in range(len(TextCorpus)):
        if float(LettersCounter[letter]!=float(0)):  #ypologismos ths syxnothtas kathe grammatwn ana keimeno
            LetterDict['a'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[A,a]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['b'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[B,b]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['c'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[C,c]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['d'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[D,d]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['e'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[E,e]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['f'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[F,f]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['g'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[G,g]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['h'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[H,h]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['i'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[i,i]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['j'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[J,j]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['k'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[K,k]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['l'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[L,l]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['m'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[M,m]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['n'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[N,n]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['o'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[O,o]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['p'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[P,p]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['q'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Q,q]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['r'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[R,r]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['s'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[S,s]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['t'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[T,t]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['u'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[U,u]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['v'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[V,v]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['w'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[W,w]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['x'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[X,x]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['y'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Y,y]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['z'][letter]=(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Z,z]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
        print letter,
        sys.stdout.flush()
        print "\r",
    print('DONE!')
    return LetterDict
    del LetterDict, letter, i, LettersCounter, TextCorpus
