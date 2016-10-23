from nltk import word_tokenize
from collections import Counter
import nltk
# to prwto orisma einai to keimeno kai to deftero einai h omada postag pou tha ypologisei
def Counter(text, label):
    # xwrizoume to keimeno se lekseis/shmeia stikshs
    words = word_tokenize(text)
    # me th xrhsh ths nltk.pos_tag xaraktirizetai h kathe leksh gia to ti postag einai
    PosTags = nltk.pos_tag(words)
    # me vasei to label pou dinetai ftiaxnoume thn kathgoria twn postags
    # xrhsimopoioume thn lista Sublabels gia na orisoume poia postags periexei kathe kathgoria

    if label == 'Noun':
        Sublabels = ['NN', 'NNS', 'NNP', 'NNPS']
    elif label == 'Pronoun':
        Sublabels = ['PRP', 'WP', 'WP$', 'PRP$']
    elif label == 'Adjective':
        Sublabels = ['JJ', 'JJS', 'JJR']
    elif label == 'Verb':
        Sublabels = ['VBG', 'VBD', 'VBN', 'VBP', 'VBZ', 'VB']
    elif label == 'Adverb':
        Sublabels = ['RB', 'WRB', 'RBS', 'RBR']
    elif label == 'Preposition':
        Sublabels = ['TO', 'IN']
    elif label == 'Conjunction':
        Sublabels = ['CC']
    elif label == 'Interjection':
        Sublabels = ['UH']
    elif label == 'Determinant':
        Sublabels = ['DT', 'WDT']
    elif label == 'Particle':
        Sublabels = ['RP']
    else:
        Sublabels = []
        print "false"
    # arxikopoioume ton counter
    count = 0
    # elegxoume an exoume tis zhtoumenes ypokathgories
    # kai an nai afksanoyme ton counter me thn antistoixh timh tous
    for i,j in PosTags:
        for k in Sublabels:
            # print k, " ", j
            if k == j:
                count += 1
    # ayth h synarthsh epistrefei ton aritho twn postags
    # me allh synarthsh tha ypologisoyme to pososto
    return count
