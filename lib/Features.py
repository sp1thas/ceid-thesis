#   ===================================
#              Features
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

def Basic():
    return {
                'TextLen':[],
                'SymbolsPerChar':[],
                'PuncuationsPerChar':[],
                'SpacesPerChar':[],
                'UpperPerChar':[],
                'LettersPerChar':[],
                'DigitsPerChar':[],
                'AvgWordLen':[],
                'AvgSentencesChars':[],
                'AvgSentencesWords':[],
                'CharsINWords':[],
                'HapaxLegomena':[],
                'HapaxDislegomena': [],
                'ShortWords': [],
                'TotalDiffWords':[],
                'TotalCharsInWords':[]
            }
def Counters():
    return {
                'Symbols':[],
                'Puncuations':[],
                'Spaces':[],
                'Upper':[],
                'Letters':[],
                'Digits':[],
                'Words':[],
                'ShortWords': []
    }
