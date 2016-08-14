import codecs, arff, sys
import unicodecsv as csv
from itertools import izip
from nltk.tokenize import RegexpTokenizer
import nltk.data
from encodings.utf_8 import decode
words_count = []    # lista me ton arithmo twn leksewn ana keimeno
word = []   # lista me tis lekseis ana keimeno
spaces_count = []   # lista gia metrima twn kenwn
textClass = []
symbols_count = []  # lista gia metrimo twn symbolwn
symbols_count_per_char = []
avg_sentences_chars = []  # lista gia meso oro protasewn os pros toy xarakthres
avg_sentences_words = []  # lista gia meso oro protasewn os pros tis lekseis
upper_count = []    # lista gia metrima twn kefalaiwn grammatwn
upper_count_per_char = []
avg_word_len = []   # lista gia metrima toy mesou orou toy mhkous twn leksewn
letters_count = []  # lista gia to metrina twn grammatwn
letters_count_per_char = []
short_words_counter = []    # lista gia to metrima twn mikrwn leksewn (<4)
digits_count = []   # lista gia to metrima twn psifion
digits_count_per_char = []
text_len = []   # megethos string toy katharoy keimenou (grammata, arithmoi, kena, symvola, ola)
freq_letter = dict()    # leksiko gia th syxnothta emfanishs grammatwn
total_chars_in_words = []   # total number of chars in word
text = []   # lista gia to katharo keimeno
ids = []    # lista gia ta ids
temp = []
punctuations_count = []
sample_read = csv.reader(open("dataset-vaso.csv","rb")) # anoigma to dataset csv
punct1 = punct2 = punct3 = punct4 = punct5 = punct6 = punct7 = punct8 = []
freq_a=freq_b=freq_c=freq_d=freq_e=freq_f=freq_g=freq_h=freq_i=freq_j=freq_k=freq_l=freq_m=freq_n=freq_o=freq_p=freq_q=freq_r=freq_s=freq_t=freq_v=freq_u=freq_w=freq_x=freq_y=freq_z=[]
symbol1=symbol2=symbol3=symbol4=symbol5=symbol6=symbol7=symbol8=symbol9 = []
symbol10=symbol11=symbol12=symbol13=symbol14=symbol15=symbol16=symbol17 = []
symbol18=symbol19=symbol20=symbol21 = []

total_diff_words = []
hapax_legomena = []
hapax_dislegomena = []
freq_word = []
write = codecs.open("text", "wb", "utf-8")
write_open = codecs.open("text", "rb", "utf-8")




def str2float_lst(lst):
    for i in range(len(lst)):
        lst[i]=float(lst[i])
    return lst


co = 0
# diavazw to object me to katharo keimeno
print('Dataset reading processing...')
for row in sample_read:
    # lista me to katharo keimeno
    text.append(row[1])  # pernaw sti lista text to katharo keimeno
    # lista me ta ids twn keimenwn
    ids.append(int(row[0]))  # to antistoixo id
    print co,
    sys.stdout.flush()
    print "\r",
    co = co+1


del sample_read
print('DONE!')
print 'megethos dataset: ', len(text)


sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

punctuations_count_per_char = []
spaces_count_per_char = []
i=[]
print('Basic feature processing...')
for i in range(len(text)):
    # ypologismos arithmou xarakthrwn ana keimeno
    text_len.append(len(text[i]))   # lista me ton arithmo xaraktirwn
    # ypologismos toy arithmou twn symvolwn ana keimeno
    symbols_count.append(len(RegexpTokenizer(r'[+/\-@&*{}\[\[|]').tokenize(text[i])))
    symbols_count_per_char.append(float(format(symbols_count[i]/float(text_len[i]), '.3f')))
    # ypologismos toy arithmou shmeiwn stikshs ana keimeno
    punctuations_count.append(len(RegexpTokenizer(r'[,.?!;\'\":]').tokenize(text[i])))
    punctuations_count_per_char.append(float(format(punctuations_count[i]/float(text_len[i]), '.3f')))
    # ypologismos toy arithmou twn kenwn xarakthrwn ana keimeno
    spaces_count.append(len(RegexpTokenizer(r' ').tokenize(text[i])))
    spaces_count_per_char.append(float(format(spaces_count[i]/float(text_len[i]), '.3f')))
    # ypologismos toy arithmou twn kefalaiwn grammatwn ana keimeno
    upper_count.append(len(RegexpTokenizer(r'[A-Z]').tokenize(text[i])))
    upper_count_per_char.append(float(format(upper_count[i]/float(text_len[i]), '.3f')))
    # ypologismos toy arithmou twn grammatwn ana keimeno
    letters_count.append(len(RegexpTokenizer(r'[A-Z,a-z]').tokenize(text[i])))
    letters_count_per_char.append(float(format(letters_count[i]/float(text_len[i]), '.3f')))
    # ypologismos toy arithmou twn pshfiwn ana keimeno
    digits_count.append(len(RegexpTokenizer(r'[0-9]').tokenize(text[i])))
    digits_count_per_char.append(float(format(digits_count[i]/float(text_len[i]), '.3f')))
    # eisagwgh sth word twn leksewn ana keimeno
    word.append(RegexpTokenizer(r'\w+').tokenize(text[i]))
    # ypologismos toy arithmou twn leksewn ana keimeno
    words_count.append(len(word[i]))
    count = 0   # metritis gia tis mikres lekseis
    count1 = 0  # metritis gia to mhkos ths kathe leksis
    for j in word[i]:

        # j = j.decode('utf8', 'replace')
        count1 += len(j)    #afkshsh toy metrith toso oso to mhkos ths lekshs
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
    total_chars_in_words.append(float(format(count1/float(text_len[i]), '.3f')))
    if words_count[i]!=0:
        # ypologismos toy mesou orou toy mhkous ths kathe lekshs
        avg_word_len.append(float(format(total_chars_in_words[i]/float(words_count[i]), '.3f')))
        # ypologismos mesou orou protasewn ana lekseis ana keimeno
        avg_sentences_words.append(float(format(len(sent_detector.tokenize(text[i]))/float(words_count[i]), '.3f')))
        # sth lista pernaw ton arithmo mikrwn leksewn kathe keimenou
        short_words_counter.append(float(format(count/float(words_count[i]), '.3f')))
        hapax_legomena.append(float(format(count_legomena/float(words_count[i]), '.3f')))
        hapax_dislegomena.append(float(format(count_dislegomena/float(words_count[i]), '.3f')))
        total_diff_words.append(float(format(len(freq_word[i])/float(words_count[i]), '.3f')))
    else:
        #print i
        avg_word_len.append(0.0)
        avg_sentences_words.append(0.0)
        short_words_counter.append(0.0)
        hapax_legomena.append(0.0)
        hapax_dislegomena.append(0.0)
        total_diff_words.append(0.0)
    if text_len[i]!=0:
        # ypologismos mesou orou protasewn ana xarakthres ana keimeno
        avg_sentences_chars.append(float(format(len(sent_detector.tokenize(text[i]))/float(text_len[i]), '.3f')))
    elif text_len[i]==0:
        print i
        avg_sentences_chars.append(0)
    print i,
    sys.stdout.flush()
    print "\r",
print('DONE!')
del word, i, words_count, spaces_count, upper_count
print('Frequency grammatwn processing...')

#                     ypologismos synxothtas emfanhshs grammatwn
for letter in range(len(text)):
    if float(letters_count[letter]) == float(0):  # an sto keimeno den emfanizontai grammata
        freq_a.append(0.0)            # h syxnothta olwn twn grammatwn einai 0
        freq_b.append(0.0)
        freq_c.append(0.0)
        freq_d.append(0.0)
        freq_e.append(0.0)
        freq_f.append(0.0)
        freq_g.append(0.0)
        freq_h.append(0.0)
        freq_i.append(0.0)
        freq_j.append(0.0)
        freq_k.append(0.0)
        freq_l.append(0.0)
        freq_m.append(0.0)
        freq_n.append(0.0)
        freq_o.append(0.0)
        freq_p.append(0.0)
        freq_q.append(0.0)
        freq_r.append(0.0)
        freq_s.append(0.0)
        freq_t.append(0.0)
        freq_u.append(0.0)
        freq_v.append(0.0)
        freq_w.append(0.0)
        freq_x.append(0.0)
        freq_y.append(0.0)
        freq_z.append(0.0)
    elif float(letters_count[letter]!=float(0)):  #ypologismos ths syxnothtas kathe grammatwn ana keimeno
        freq_a.append(float(format(len(RegexpTokenizer(r'[A,a]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_b.append(float(format(len(RegexpTokenizer(r'[B,b]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_c.append(float(format(len(RegexpTokenizer(r'[C,c]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_d.append(float(format(len(RegexpTokenizer(r'[D,d]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_e.append(float(format(len(RegexpTokenizer(r'[E,e]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_f.append(float(format(len(RegexpTokenizer(r'[F,f]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_g.append(float(format(len(RegexpTokenizer(r'[G,g]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_h.append(float(format(len(RegexpTokenizer(r'[H,h]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_i.append(float(format(len(RegexpTokenizer(r'[i,i]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_j.append(float(format(len(RegexpTokenizer(r'[J,j]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_k.append(float(format(len(RegexpTokenizer(r'[K,k]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_l.append(float(format(len(RegexpTokenizer(r'[L,l]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_m.append(float(format(len(RegexpTokenizer(r'[M,m]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_n.append(float(format(len(RegexpTokenizer(r'[N,n]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_o.append(float(format(len(RegexpTokenizer(r'[O,o]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_p.append(float(format(len(RegexpTokenizer(r'[P,p]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_q.append(float(format(len(RegexpTokenizer(r'[Q,q]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_r.append(float(format(len(RegexpTokenizer(r'[R,r]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_s.append(float(format(len(RegexpTokenizer(r'[S,s]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_t.append(float(format(len(RegexpTokenizer(r'[T,t]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_u.append(float(format(len(RegexpTokenizer(r'[U,u]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_v.append(float(format(len(RegexpTokenizer(r'[V,v]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_w.append(float(format(len(RegexpTokenizer(r'[W,w]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_x.append(float(format(len(RegexpTokenizer(r'[X,x]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_y.append(float(format(len(RegexpTokenizer(r'[Y,y]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
        freq_z.append(float(format(len(RegexpTokenizer(r'[Z,z]').tokenize(text[letter]))/float(letters_count[letter]), '.3f')))
    print letter,
    sys.stdout.flush()
    print "\r",

print('DONE!')
# # leksiko sto opoio apothikevetai h syxnothta twn grammatwn ana keimeno
freq_letter = {'a': freq_a, 'b': freq_b, 'c': freq_c, 'd': freq_d, 'e': freq_e, 'f': freq_f, 'g': freq_g, 'h': freq_h, 'i': freq_i, 'j': freq_j, 'k': freq_k, 'l': freq_l, 'm': freq_m, 'n': freq_n, 'o': freq_o, 'p': freq_p, 'q': freq_q, 'r': freq_r, 's': freq_s, 't': freq_t, 'u': freq_u, 'v': freq_v, 'w': freq_w, 'x': freq_x, 'y': freq_y, 'z': freq_z}
del freq_a, freq_b, freq_c, freq_d, freq_e, freq_f, freq_g, freq_h, freq_i, freq_j, freq_k, freq_l, freq_m, freq_n, freq_o, freq_p, freq_q, freq_r, freq_s, freq_t, freq_u, freq_v, freq_w, freq_x, freq_y, freq_z
del letters_count

################### YPOLOGISMOS SYXNOTHTAS SYMVOLWN ##########################

print('Symbols frequency processing...')
for symbol in range(len(text)):     # an sto keimeno den emfanizetai kanena
    if symbols_count[symbol]==0:    # symvolo tote h syxnothta twn symvolwn einai 0
        symbol1.append(0.0)
        symbol2.append(0.0)
        symbol3.append(0.0)
        symbol4.append(0.0)
        symbol5.append(0.0)
        symbol6.append(0.0)
        symbol7.append(0.0)
        symbol8.append(0.0)
        symbol9.append(0.0)
        symbol10.append(0.0)
        symbol11.append(0.0)
        symbol12.append(0.0)
        symbol13.append(0.0)
        symbol14.append(0.0)
        symbol15.append(0.0)
        symbol16.append(0.0)
        symbol17.append(0.0)
        symbol18.append(0.0)
        symbol19.append(0.0)
        symbol20.append(0.0)
        symbol21.append(0.0)
    elif symbols_count[symbol]!=0:  # ypologismos syxnothtas emfanishs symvolwn ana keimeno
        symbol1.append(float(format(len(RegexpTokenizer(r'[~]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol2.append(float(format(len(RegexpTokenizer(r'[@]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol3.append(float(format(len(RegexpTokenizer(r'[#]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol4.append(float(format(len(RegexpTokenizer(r'[$]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol5.append(float(format(len(RegexpTokenizer(r'[%]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol6.append(float(format(len(RegexpTokenizer(r'^').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol7.append(float(format(len(RegexpTokenizer(r'[&]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol8.append(float(format(len(RegexpTokenizer(r'[*]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol9.append(float(format(len(RegexpTokenizer(r'[-]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol10.append(float(format(len(RegexpTokenizer(r'[_]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol11.append(float(format(len(RegexpTokenizer(r'[=]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol12.append(float(format(len(RegexpTokenizer(r'[+]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol13.append(float(format(len(RegexpTokenizer(r'[<]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol14.append(float(format(len(RegexpTokenizer(r'[>]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol15.append(float(format(len(RegexpTokenizer(r'[{]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol16.append(float(format(len(RegexpTokenizer(r'[}]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol17.append(float(format(len(RegexpTokenizer(r'[[]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol18.append(float(format(len(RegexpTokenizer(r'[]]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol19.append(float(format(len(RegexpTokenizer(r'[/]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol20.append(float(format(len(RegexpTokenizer(r"['\']").tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
        symbol21.append(float(format(len(RegexpTokenizer(r'[|]').tokenize(text[symbol]))/float(symbols_count[symbol]), '.3f')))
    print symbol,
    sys.stdout.flush()
    print "\r",
print('DONE!')
# # sto leksiko pernaw th syxnothta emfanishs symvolwn ana keimeno
freq_symbols = {"~":symbol1, '@':symbol2, '#':symbol3, '$':symbol4, '%':symbol5, '^':symbol6, '&':symbol7, '*':symbol8, '-':symbol9, '_':symbol10, '=':symbol11, '+':symbol12, '>':symbol13, '<':symbol14, '[':symbol15, ']':symbol16, '{':symbol17, '}':symbol18, '/':symbol19, '"\"': symbol20, '|': symbol21}
del symbols_count, symbol1,symbol2,symbol3,symbol4,symbol5,symbol6,symbol7,symbol8,symbol9,symbol10,symbol11,symbol12,symbol13,symbol14,symbol15,symbol16,symbol17,symbol18,symbol19,symbol20,symbol21
#
#
#
# #                      YPOLOGISMOS SYXNOTHTAS EMFANISHS SIMEIWN STIKSEWS
#
print('Punctuations frequency processing...')
for punct in range(len(text)):
    if punctuations_count[punct]==0:  # an den emfanizetai kanena shmeio sthksews sto keimeno
        punct1.append(0)            # tote h syxnothta olwn twn shmeiwn stiksews sto keimeno einai 0
        punct2.append(0)
        punct3.append(0)
        punct4.append(0)
        punct5.append(0)
        punct6.append(0)
        punct7.append(0)
        punct8.append(0)
    else:  # ypologismos syxnothtas emfanhshs shmeiwn stiksews ana keimeno
        punct1.append(float(format(len(RegexpTokenizer(r'[,]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct2.append(float(format(len(RegexpTokenizer(r'[.]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct3.append(float(format(len(RegexpTokenizer(r'[?]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct4.append(float(format(len(RegexpTokenizer(r'[!]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct5.append(float(format(len(RegexpTokenizer(r'[:]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct6.append(float(format(len(RegexpTokenizer(r'[;]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct7.append(float(format(len(RegexpTokenizer(r'[\']').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
        punct8.append(float(format(len(RegexpTokenizer(r'[\"]').tokenize(text[punct]))/float(punctuations_count[punct]), '.3f')))
	print punct,
    sys.stdout.flush()
    print "\r",
print('DONE!')
# leksiko sto opoio pernaw sth syxnothta emfanishs twn shmeiwn stiksews ana keimeno
freq_punctuations = {",": punct2, ".": punct2, "?": punct3, "!": punct4, ":": punct5, ";": punct6, "\'": punct7, "\"": punct8}
del punct1, punct2, punct3, punct4, punct5, punct6, punct7, punct8, text, punctuations_count

# ftiaxnw to header gia to csv pou tha eksagw
header = ['text_id','text_length','symbols/char','punctuations/char','spaces/char','upper/char',
          'letters/char','digits/char','shor_words/char', 'total_chars_in_words',
          'avg_word_length','avg_sentences/word','avg_sentences/char','total_diff_words',
          'hapax_legomena','hapax_dislegomena','a_freq','b_freq','c_freq','d_freq',
          'e_freq','f_freq','g_freq','h_freq','i_freq','j_freq','k_freq','l_freq','m_freq',
          'n_freq','o_freq','p_freq','q_freq','r_freq','s_freq','t_freq','v_freq','u_freq',
          'w_freq','x_freq','y_freq','z_freq','symbol_tilde_freq','symbol_at_freq','symbol_hash_freq','symbol_dollar_freq',
          'symbol_percent_freq','symbol_caret_freq','symbol_ampersand_freq','symbol_asterisk_freq','symbol_dash_freq','symbol_dash1_freq','symbol_equals_sign_freq','symbol_plus_freq','symbol_greater_freq',
          'symbol_less_freq','punctuation_bracket1_freq','punctuation_bracket2_freq','punctuation_bracket3_freq','punctuation_bracket4_freq','punctuation_verticalbar_freq','punctuation_comma_freq',
          'punctuation_fullstop_freq','punctuation_questionmark_freq','punctuation_exclamationmark_freq','punctuation_colon_freq','punctuation_semicolon_freq','punctuation_quotationmark1_freq','punctuation_quotationmark2_freq']
print('izip object processing...')
# me izip pernaw sto output ola ta features pou einai pros eggrafh sto csv
output = izip(ids, text_len, symbols_count_per_char, punctuations_count_per_char, spaces_count_per_char,
 upper_count_per_char, letters_count_per_char, digits_count_per_char, short_words_counter, total_chars_in_words,
 avg_word_len, avg_sentences_words, avg_sentences_chars, total_diff_words, hapax_legomena, hapax_dislegomena,
 freq_letter["a"], freq_letter["b"], freq_letter["c"],
 freq_letter["d"], freq_letter["e"], freq_letter["f"], freq_letter["g"],
 freq_letter["h"], freq_letter["i"], freq_letter["j"], freq_letter["k"],
 freq_letter["l"], freq_letter["m"], freq_letter["n"], freq_letter["o"],
 freq_letter["p"], freq_letter["q"], freq_letter["r"], freq_letter["s"],
 freq_letter["t"], freq_letter["u"], freq_letter["v"], freq_letter["w"],
 freq_letter["x"], freq_letter["y"], freq_letter["z"], freq_symbols["~"],
 freq_symbols['@'], freq_symbols['#'], freq_symbols['$'], freq_symbols['%'],
 freq_symbols['^'], freq_symbols['&'], freq_symbols['*'], freq_symbols['-'],
 freq_symbols['_'], freq_symbols['='], freq_symbols['+'], freq_symbols['>'],
 freq_symbols['<'], freq_symbols['['], freq_symbols[']'], freq_symbols['{'],
 freq_symbols['}'], freq_symbols['|'],
 freq_punctuations[","], freq_punctuations["."], freq_punctuations["?"],
 freq_punctuations["!"], freq_punctuations[":"], freq_punctuations[";"],
 freq_punctuations["\'"], freq_punctuations["\""] )
print('DONE!')

del ids, text_len, symbols_count_per_char, punctuations_count_per_char, spaces_count_per_char, textClass
del upper_count_per_char, letters_count_per_char, digits_count_per_char, short_words_counter, total_chars_in_words
del avg_word_len, avg_sentences_words, avg_sentences_chars, total_diff_words, hapax_legomena, hapax_dislegomena,freq_letter
del freq_symbols, freq_punctuations
print('Eggrafi arxeiou arff')
arff.dump("result2.arff", output, relation='results', names=header)
del output, header
print('DONE!')
print('TELOS - BE HAPPY :)')
