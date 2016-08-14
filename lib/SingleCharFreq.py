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
    FreqDict = { '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[] }
    print('Puncuations frequency processing...')
    for punct in range(len(TextCorpus)):
        if PunctCounter[punct] == 0:  # an den emfanizetai kanena shmeio sthksews sto keimeno
            for i in FreqDict:
                FreqDict[i].append(0.0)
        elif PunctCounter[punct] > 0 :  # ypologismos syxnothtas emfanhshs shmeiwn stiksews ana keimeno
            FreqDict['1'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[,]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['2'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[.]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['3'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[?]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['4'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[!]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['5'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[:]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['6'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[;]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['7'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\']').tokenize(TextCorpus[punct])), PunctCounter[punct]))
            FreqDict['8'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\"]').tokenize(TextCorpus[punct])), PunctCounter[punct]))
        print punct,
        sys.stdout.flush()
        print "\r",
    print('Done')
    return FreqDict
    del FreqDict, TextCorpus, punct, PunctCounter, i



'''
    Synartisi gia ton ypologismo twn features gia ta symvola
    pernei ws orisma to text kai epistrefei ena dictionary me tis
    metriseis gia kathe ena symvolo
'''
def SymbolChars(TextCorpus, TextLen, SymbolsCounter):
    print('Symbols frequency processing...')
    SymbolDict = { '1':[], '2':[], '3':[], '4':[], '5':[], '6':[], '7':[], '8':[],
                '9':[], '10':[], '11':[], '12':[], '13':[], '14':[], '15':[], '16':[],
                '17':[], '18':[], '19':[], '20':[], '21':[] }
    for symbol in range(len(TextCorpus)):     # an sto keimeno den emfanizetai kanena
        if TextLen[symbol]==0:    # symvolo tote h syxnothta twn symvolwn einai 0
            for i in SymbolDict:
                SymbolDict[i].append(0.0)
        elif TextLen!=0:  # ypologismos syxnothtas emfanishs symvolwn ana keimeno
            SymbolDict['1'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[~]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['2'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[@]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['3'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[#]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['4'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[$]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['5'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[%]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['6'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[\^]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['7'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[&]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['8'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[*]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['9'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[-]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['10'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[_]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['11'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[=]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['12'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[+]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['13'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[<]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['14'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[>]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['15'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[{]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['16'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[}]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['17'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[[]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['18'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[]]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['19'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[/]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['20'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r"['\']").tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
            SymbolDict['21'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[|]').tokenize(TextCorpus[symbol])),SymbolsCounter[symbol]))
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
    LetterDict = { 'a':[], 'b':[], 'c':[], 'd':[], 'e':[], 'f':[], 'g':[], 'h':[],
               'i':[], 'j':[], 'k':[], 'l':[], 'm':[], 'n':[], 'o':[], 'p':[],
               'q':[], 'r':[], 's':[], 't':[], 'u':[], 'v':[], 'w':[], 'x':[],
               'y':[], 'z':[] }

    for letter in range(len(TextCorpus)):
        if float(LettersCounter[letter]) == float(0):  # an sto keimeno den emfanizontai grammata
            for i in LetterDict:
                LetterDict[i].append(0.0)
        elif float(LettersCounter[letter]!=float(0)):  #ypologismos ths syxnothtas kathe grammatwn ana keimeno
            LetterDict['a'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[A,a]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['b'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[B,b]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['c'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[C,c]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['d'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[D,d]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['e'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[E,e]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['f'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[F,f]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['g'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[G,g]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['h'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[H,h]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['i'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[i,i]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['j'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[J,j]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['k'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[K,k]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['l'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[L,l]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['m'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[M,m]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['n'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[N,n]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['o'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[O,o]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['p'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[P,p]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['q'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Q,q]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['r'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[R,r]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['s'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[S,s]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['t'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[T,t]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['u'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[U,u]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['v'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[V,v]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['w'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[W,w]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['x'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[X,x]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['y'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Y,y]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
            LetterDict['z'].append(PercentCalc.PercentCalc(len(RegexpTokenizer(r'[Z,z]').tokenize(TextCorpus[letter])), LettersCounter[letter]))
        print letter,
        sys.stdout.flush()
        print "\r",
    print('DONE!')
    return LetterDict
    del LetterDict, letter, i, LettersCounter, TextCorpus
