#   ===================================
#               PercentCalc
#   ===================================

__author__ = "Simakis Panagiotis"
__license__ = "GPL"
__email__ = "sp1thas@autistici.org"

def PercentCalc( Count, Sum ):
    if Sum > 0.0:
        return float(format(Count/float(Sum), '.3f'))
    else:
        return 0.0
