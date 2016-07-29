def PercentCalc( Count, Sum ):
    if Sum > 0.0:
        return float(format(Count/float(Sum), '.3f'))
    else:
        return 0.0