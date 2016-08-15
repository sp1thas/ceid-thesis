#   ===================================
#              Features
#   ===================================
__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

def Basic(length):
    return {
                'TextLen':[0.0]*length,
                'SymbolsPerChar':[0.0]*length,
                'PuncuationsPerChar':[0.0]*length,
                'SpacesPerChar':[0.0]*length,
                'UpperPerChar':[0.0]*length,
                'LettersPerChar':[0.0]*length,
                'DigitsPerChar':[0.0]*length,
                'AvgWordLen':[0.0]*length,
                'AvgSentencesChars':[0.0]*length,
                'AvgSentencesWords':[0.0]*length,
                'CharsINWords':[0.0]*length,
                'HapaxLegomena':[0.0]*length,
                'HapaxDislegomena': [0.0]*length,
                'ShortWords': [0.0]*length,
                'TotalDiffWords':[0.0]*length,
                'TotalCharsInWords':[0.0]*length
            }
def Counters(length):
    return {
                'Symbols':[0.0]*length,
                'Puncuations':[0.0]*length,
                'Spaces':[0.0]*length,
                'Upper':[0.0]*length,
                'Letters':[0.0]*length,
                'Digits':[0.0]*length,
                'Words':[0.0]*length,
                'ShortWords': [0.0]*length
    }
